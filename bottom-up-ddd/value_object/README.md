## ValueObject

属性を表現するクラス。又は、``特殊化された型``とも言えます。

クラスでユーザーを表現しようとした時に、以下の要素が属性として入るとする。
- 氏名
- 電話番号
- 誕生日

これらの要素を文字列型や日付型といった汎用的な型で表現するよりも、氏名型、電話番号型、誕生日型といった``特殊な型``があった方がやりやすいと考える。
こういった特殊な型がValueObjectである。


## ValueObjectのルール
基本的に以下のような原則があります。

- 状態を不変に保つ
- 同じ値オブジェクト同士で値が等しいかどうかの確認ができる
- 完全に交換可能

#### 状態を不変に保つ
インスタンスを生成した後は、値(状態)の変更をできないようにする。
「状態を不変に保てる」というルールに照らし合わせると、値オブジェクトに相応しい実装はイミュータブルなクラス


値を不変にすることで以下のメリットもある
- フィールドが変更されることを考慮せずに済む
- 並列や並行で実行した際に状態が変更される恐れがない
- キャッシュしてメモリを節約することが可能になる

#### 同じ値オブジェクト同士で値が等しいかどうかの確認ができる

#### 完全に交換可能


## ValueObjectはどういう状況で作るべきか
- 値に振る舞いを持たせたい時
- 「存在しない値を存在させない」
- 「間違った代入を防ぐ」




## Userクラスを題材にした例

名前を持つユーザークラスを題材に考える。以下のようになる。
至ってシンプルであるが、「ユーザー名が 3 文字以上である」という制約があった場合にはどのように実装することになるか。

```
class User:
    def __init__(self, name : str):
        self.name = name

    def change_name(self, name : str):
        self.name = name
```

シンプルに、「ユーザー名が3文字以上か」というチェック機構を組み込むと以下のようになるはずです。

```
class User:
    def __init__(self, name : str):
        if len(name) < 3:
            raise Exception('throw argument name')
        self.name = name

    def change_name(self, name : str):
        if len(name) < 3:
            raise Exception('throw argument name')
        self.name = name

```

お次に電話番号を登録できるようにしていきます。
当然ですが、チェック機構も含めると以下のようになります。

```
import re

class User:
    def __init__(self, name : str):
        if len(name) < 3:
            raise Exception('throw argument name')
        self.name = name

        self.phone_number = None

    def change_name(self, name : str):
        if len(name) < 3:
            raise Exception('throw argument name')
        self.name = name

    def change_phone_number(self, phone_number : str):
        pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
        result = re.match(pattern, phone_number)
        if result is None:
            raise Exception('throw argument phone_number')
        self.phone_number = phone_number
```

チェック機構などの処理をどんどん足していくと、クラスが複雑化していきます。

Userクラスとは別で、追加で企業情報のクラスを作成します。Userクラス同様に電話番号登録が出来るようにすると以下のようになります。

```
import re

class Company:
    def __init__(self):
        self.phone_number = None

    def change_phone_number(self, phone_number : str):
        pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
        result = re.match(pattern, phone_number)
        if result is None:
            raise Exception('throw argument phone_number')
        self.phone_number = phone_number
```

ここで問題なのは、``電話番号の正規表現``が両方のクラスで記述されるようになったことです。

これでは、電話番号の桁数が増えた場合の修正が入った際に、多くの場所に修正が広がるようになります。


他にもUserクラスとCompanyクラスに``電話番号が携帯電話番号かをチェックする``機構を加えてみます。

```

import re
class User:
    def __init__(self, name : str):
        if len(name) < 3:
            raise Exception('throw argument name')
        self.name = name

        self.phone_number = None

    def change_name(self, name : str):
        if len(name) < 3:
            raise Exception('throw argument name')
        self.name = name

    def change_phone_number(self, phone_number : str):
        pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
        result = re.match(pattern, phone_number)
        if result is None:
            raise Exception('throw argument phone_number')
        self.phone_number = phone_number

    def is_mobile_phone(self):
        pattern = '^(070|080|090)-\d{4}-\d{4}$'
        result = re.match(pattern, phone_number)
        return True if result is not None else False

class Company:
    def __init__(self):
        self.phone_number = None

    def change_phone_number(self, phone_number : str):
        pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
        result = re.match(pattern, phone_number)
        if result is None:
            raise Exception('throw argument phone_number')
        self.phone_number = phone_number

    def is_mobile_phone(self):
        pattern = '^(070|080|090)-\d{4}-\d{4}$'
        result = re.match(pattern, phone_number)
        return True if result is not None else False

```

上記二つのクラスに、携帯電話番号かをチェックする処理がそれぞれ記述されてしまっています。
これでは携帯電話番号かをチェックする処理に修正する場合に、複数ヶ所を修正しなくてはいけなくなります。

こういった状況を回避するために、ValueObjectを利用します。これにより、変更に強いコードを書くことが可能になります。

氏名型、電話番号型などといった特殊化された型を使用します。

```

class UserName:
    def __init__(self, name: str):
        if len(name) < 3:
            raise Exception('throw argument name')
        self.value = name


class PhoneNumber:
    def __init__(self, phone_number: str):
        pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
        result = re.match(pattern, phone_number)
        if result is None:
            raise Exception('throw argument phone_number')
        self.full = phone_number

    def is_mobile_phone(self):
        pattern = '^(070|080|090)-\d{4}-\d{4}$'
        result = re.match(pattern, self.full)
        return True if result is not None else False

```

上記を見ればUserName,PhoneNumberという特殊化された型を作成しました。
上記のような型を以下のようにして使用します。

```
class User:
    def __init__(self, name: UserName):
        if name is None:
            raise Exception('ArgumentNullException name')
        self.name = name

    def change_name(self, name: UserName):
        if name is None:
            raise Exception('ArgumentNullException name')
        self.name = name

    def phone_number(self, phone_number: PhoneNumber):
        if phone_number is None:
            raise Exception('ArgumentNullException phone_number')
        self.phone_number = phone_number


class Company:
    def change_phone_number(self, phone_number: PhoneNumber):
        if phone_number is None:
            raise Exception('ArgumentNullException phone_number')
        self.phone_number = phone_number
```

上記のような使い方をすることで、電話番号関連の修正がPhoneNumberクラスを修正するだけで良くなり、「ユーザー名を5文字以上に制限する」などといった修正もUserNameクラスを修正するだけでよくなります。


### 参考源
- [[DDD]ValueObject](https://nrslib.com/valueobject/)
- [ボトムアップドメイン駆動設計 : 値オブジェクト](https://nrslib.com/bottomup-ddd/#outline__3_1)
- [PythonでボトムアップDDD 【値オブジェクト】](https://qiita.com/kotamatsuoka/items/832ffe97e2a1c19141b4#%E5%80%A4%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E3%83%AB%E3%83%BC%E3%83%AB)
