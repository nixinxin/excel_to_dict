A small package to convert record in excel into dict.
* 打包
    * 先编译包 python setup.py build
    * 打包成源代码 python setup.py sdist build
    * 生成egg包 python setup.py bdist_egg
    * 生成wheel包 python setup.py sdist bdist_wheel
* 发布包
    ```
    # 发布 .tar.gz 包
    $ python setup.py sdist upload 
    # 发布 egg 包
    $ python setup.py bdist_egg upload 
    # 发布 wheel 包
    $ python setup.py bdist_wheel upload
    $ twine upload dist/* 主要用该命令
    ```
