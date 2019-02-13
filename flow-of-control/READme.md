# Using Python Flow of control in Clean Architecture
Clean Architectureの右下の図にあるflow of controlについて解説し、サンプルコードをPythonで実装してみました。
元々は、DDDをわかりやすく解説している[こちらの記事](https://nrslib.com/clean-flow-of-control/)のサンプルコードをPythonで実装し、自分なりの補足などをまとめた内容です。

flow of controlとは読んで字のごとく、「制御の流れ」という意味で、プログラムの処理の順番のことです。
図で見れば、Flow of controlは、Controller -> UseCaseInteractor -> Presenterの順番で処理が進んでいくことを示しています。

### クラス構成
flow of control以外にも白抜きや黒などの矢印を指しているものがあります。矢印は、いわゆる依存関係というものを表している図です。
Controllerは、UseCaseInputPortに依存していることを表しています。


### クラスでみる制御の流れ
- 1.ControllerがUseCaseInputPort(interface)を利用する（メソッドを呼ぶ）
- 2.UseCaseInputPort の実装である UseCaseInteractor の処理が実行される
- 3.UseCaseInteractor は処理の結果を UseCaseOutputPort に伝える
- 4.UseCaseOutputPort の実装である Presenter において、出力が表現される

Controller -> UseCaseInteractor -> Presenterという順序で実行されているため、flow of control通りの制御の流れになっている。

---

### 実際のソースコード
- Controllerに該当

[interface_adapters/controller.py](./interface_adapters/controller.py) Controllerクラス

コンストラクタで。IEditStringUseCase型のオブジェクトであるinput_portを受け取る。
IEditStringUseCaseは、flow of controlでいうUseCaseInputPortである。

IEditStringUseCaseクラス自体は抽象クラスであり、具体的な実装を持っていない。
input_portで受け取ったオブジェクトは、IEditStringUseCaseを継承した具象オブジェクト。

ちなみにIEditStringUseCaseを継承した具象オブジェクトは、UseCaseInteractorのことです。
executeメソッドで、UseCaseInteractorに該当するオブジェクトのhandleメソッドを実行していることがわかります。

```
# -*- coding: utf-8 -*-
from application_business_rules.interface_input_output import IEditStringUseCase


class Controller:
    def __init__(self, input_port : IEditStringUseCase):
        self.__input_port = input_port

    def execute(self, source : list)->None:
        self.__input_port.handle(source)

```

- UseCaseInputPortに該当

[application_business_rules/interface_input_output.py](./application_business_rules/interface_input_output.py) IEditStringUseCaseクラス

インターフェースに該当するものですが、Pythonにはインターフェースの機能がないため、抽象クラスで再現します。

IEditStringUseCase型を継承した具象クラスは、handleメソッドを実装させることを強制させます。
UseCaseInteractorに該当するクラスにIEditStringUseCase型を継承させます。

```
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class IEditStringUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, data : list)->None:
        pass

```

- UseCaseInteractorに該当

[application_business_rules/usecase.py](./application_business_rules/usecase.py) ToCsvUseCase,ToTsvUseCase クラス

ロジックを記述するクラスです。ToCsvUseCase,ToTsvUseCaseのどちらもIEditStringUseCaseを継承していることがわかります。
flow of controlの白抜きの矢印の図は``関連``を表しています。

コンストラクタでは、IEditStringOutputPort型のオブジェクトであるoutput_portを受け取る。
IEditStringOutputPortは、flow of controlでいうUseCaseOutputPortである。

IEditStringOutputPortクラス自体も抽象クラスであり、具体的な実装は持っていない。
output_portで受け取ったオブジェクトは、IEditStringOutputPortを継承した具象オブジェクト。

ちなみにIEditStringOutputPortを継承した具象オブジェクトは、Presenterのことです。
handleメソッドで、UseCaseOutputPortに該当するオブジェクトのemitメソッドを実行していることがわかります。

flow of controlの図でわかる通り、UseCaseOutputPort型の抽象クラス(インターフェース)を利用しています。
これによってわかるのは、UseCaseInteractorに該当するToCsvUseCase,ToTsvUseCaseのどちらも具象クラスには依存していないことがわかる。
あくまでも抽象クラス(インターフェース)に依存していることがわかります。

```
# -*- coding: utf-8 -*-
from application_business_rules.interface_input_output import IEditStringOutputPort, IEditStringUseCase


class ToCsvUseCase(IEditStringUseCase):

    def __init__(self, output_port : IEditStringOutputPort):
        self.__output_port = output_port

    def handle(self, data : list)->None:
        result = None
        result = ','.join(data)
        self.__output_port.emit(result)

class ToTsvUseCase(IEditStringUseCase):

    def __init__(self, output_port : IEditStringOutputPort):
        self.__output_port = output_port

    def handle(self, data : list)->None:
        result = '\t'.join(data)
        self.__output_port.emit(result)

```

- UseCaseOutputPortに該当

[application_business_rules/interface_input_output.py](./application_business_rules/interface_input_output.py) IEditStringOutputPortクラス

インターフェースに該当するものですが、Pythonにはインターフェースの機能がないため、抽象クラスで再現します。

IEditStringOutputPort型を継承した具象クラスは、emitメソッドを実装させることを強制させます。
Presenterに該当するクラスにIEditStringOutputPort型を継承させます。

```
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class IEditStringOutputPort(metaclass=ABCMeta):
    @abstractmethod
    def emit(self, data : str)->None:
        pass
```


- Presenterに該当

[interface_adapters/presenter.py](./interface_adapters/presenter.py) ConsolePresenter,SaveToFilePresenterクラス

出力部分を表示するクラス。UseCaseOutputPortに該当するIEditStringOutputPort型を継承している。
ConsolePresenterもSaveToFilePresenterも抽象クラスであるIEditStringOutputPortに``関連``することになる。

```
# -*- coding: utf-8 -*-
import os

from application_business_rules.interface_input_output import IEditStringOutputPort

class ConsolePresenter(IEditStringOutputPort):

    def emit(self, data : str)->None:
        print(data)

class SaveToFilePresenter(IEditStringOutputPort):
    __FILE_PATH = "out.txt"

    def emit(self, data : str)->None:
        file = open(self.__FILE_PATH, 'w')
        file.write(data)
        file.close()

```


## 参考資料

- [クリーンアーキテクチャの右下の図](https://nrslib.com/clean-flow-of-control/)