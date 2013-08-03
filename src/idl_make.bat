rem python ..\tce2py.py -i ..\idl\tce1.txt -o tce1.py
python ..\tce\tce2py.py -i .\idl\newgis.idl -o newgis.py
python ..\tce\tce2as.py -i .\idl\newgis.idl -o .\lib\flex -p newgis -filter "IAuthService- IGatewayAdapter- IUserService- IAoModuleCtrl- ICtrlService- IAoModuleCtrl- IUserClient"
python ..\tce\tce2as.py -i .\idl\newgis.idl -o .\flex\newgis\src -p newgis -filter "IAuthService- IGatewayAdapter- IUserService- IAoModuleCtrl- ICtrlService- IAoModuleCtrl- IUserClient"

mkdir .\flex\newgis\src\tcelib
xcopy ..\tce\actionscript\tcelib .\flex\newgis\src\tcelib /s /e /y

mkdir .\flex\newgis_gd\src\tcelib
xcopy ..\tce\actionscript\tcelib .\flex\newgis_gd\src\tcelib /s /e /y

