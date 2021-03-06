
### ドメイン駆動設計の定義
- Focus on the core complexity and opportunity in the domain(ドメイン内で中核となる複雑さと機会に焦点を当てる)
- Explore models in a collaboration of domain experts and software experts(ドメイン専門家とソフトウェア専門家のコラボレーションでモデルを探る)
- Write software that expresses those models explicitly(明示的にそれらのモデルを表現するソフトウェアを書く)
- Speak ubiquitous language within a bounded context(境界付けられたコンテキストの中でユビキタス言語で話す)


#### 不変条件
業務の制約について考える時に[不変条件]というものについて考える。


- 不変条件とは、モデルが有効である期間中、常に一貫している必要のある状態のこと


仕様、制約条件といった様々な呼び方があるものの、DDDの用語としては不変条件と言う言葉をよく使う。

#### 不変条件を満たすモデルを実装する
以下の不変条件を満たすモデルを実装してみます。例としてタスクアプリケーションを作成してみます。

- タスクは必ずタスク名、期日を持つ
- タスクは未完了状態で作成し、完了したら戻すことはできない
- タスクは3回だけ、1日ずつ延期することができる。
- タスク名は変更することができない

##### ドメインの知識を表現していないモデル（不変条件を破っている)
実際に上記のモデルを作成したものの、よくやりがちなのがsetter/getterメソッド類を並べてしまうことです。
下記のdomain.py内にあるTaskクラスはsetter/getterを大量に定義していますが、あまり良いやり方とは言えません。

- [bad_domain_model/domain.py](/bad_domain_model/domain.py)

実際に上記のドメインモデルを扱うアプリケーションクラスであるTaskApplicationを実装してみて、一応問題はありません。
しかし、上記のTaskクラスようなドメインモデルでは、AnotherTaskApplicationクラスのような不変条件を破るコードを生みだす可能性があります。
- [bad_domain_model/application.py](/bad_domain_model/domain.py)


不変条件を表現できていないこのオブジェクトは、もはやモデルではなく、リレーショナルモデルをオブジェクトに投影した単なる``データモデル``にすぎません。
このようなアプリケーションは、``トランザクションスクリプト``と言えます。

##### ドメインの知識を表現しているモデル（不変条件を満たしている)
そこで不変条件を満たしたモデルを実装してみると下記のようになります。

[good_domain_model/domain.py](/good_domain_model/domain.py)

上記のdomain.py内にあるTaskクラスはsetterクラスを設けていないため、簡単には値の変更ができないようになっています。
値の入力を受け付けるのはコンストラクタからのみで、状態遷移がある際はドメインモデル内に実装しています。(外から属性値を変更させない)

ドメインを操作するアプリケーションクラスの実装は以下のようになっています。
アプリケーションクラスのコードを見ればわかりますが、不変条件を破った状態遷移のコードが実装できないようになっています。

[good_domain_model/application.py](/good_domain_model/application.py)

###### 上記の実装の特徴
- Taskクラスを読むだけで、Taskモデルの不変条件が理解できる
- アプリケーションでどのようなコードを書こうが、不変条件を破った状態遷移をさせることができない
- レビュー時にもこのクラスだけ見れば安心
- 1クラス単体テストで不変条件保持の担保ができる

### まとめ

モデルが、どのような振る舞いをするのか、仕様変更時にどう変わるのか。
それらを業務のエキスパートと言葉の定義を合わせ、常に最新の、より表現力の高いモデルを追求して、コードを追従させていく。
それがドメイン駆動設計である。

---

参考資料
- [モデルでドメイン知識を表現するとは何か[DDD]](https://little-hands.hatenablog.com/entry/2017/10/04/201201)