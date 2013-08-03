====================================================
脱离django环境使用django的数据持久化功能 
设置环境变量 :  set DJANGO_SETTINGS_MODULE=newgis.settings
添加PYTHONPATH路径 sys.path.append('e:/works/newgis/django')
导入app ：　
  import giscore.models
  vp = giscore.models.VisitedPoint()

====================================================
geoExt-1.0
ext-3.2.0
openlayer-2.8
django-1.1
====================================================


django 默认 DataTimeField采用时区，我们采用不使用时区方式存储，
所以将postgresql/creation.py 覆盖到C:\Python26\Lib\site-packages\django\db\backends\postgresql

python django-amin startapp
python manage.py reset giscore  #创建数据库
python manage.py runserver localhost:8000

初始化数据库 ../src/das/initdb.py
