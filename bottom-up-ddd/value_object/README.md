## ValueObject

属性を表現するクラス。又は、``特殊化された型``とも言えます。

クラスでユーザーを表現しようとした時に、以下の要素が属性として入るとする。
- 氏名
- 電話番号
- 誕生日

これらの要素を文字列型や日付型といった汎用的な型で表現するよりも、氏名型、電話番号型、誕生日型といった``特殊な型``があった方がやりやすいと考える。
こういった特殊な型がValueObjectである。


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