@echo off

echo 选择操作：
echo [0]退出；[1]线稿；[2]平行线条图；[3]点图；[4]合并图片
set /p op=请输入操作编号：

if %op%==0 exit

call ./.venv/Scripts/activate.bat

if %op%==1 goto edge
if %op%==2 goto line_block
if %op%==3 goto dot_block
if %op%==4 goto combine

:edge
set /p arg1=请输入线条粗细（默认5）：
set /p arg2=请输入滤波大小（默认7）：
if "%arg1%"=="" set arg1=5
if "%arg2%"=="" set arg2=7
echo 参数 %arg1% %arg2%
python ./src/edge.py %arg1% %arg2%
goto exit_p

:line_block
set /p arg1=请输入线条粗细（默认2）：
set /p arg2=请输入密度缩放大小（默认0.1，越大越密）：
set /p arg3=请输入块大小（默认48）：
if "%arg1%"=="" set arg1=2
if "%arg2%"=="" set arg2=0.1
if "%arg3%"=="" set arg3=48
echo 参数 %arg1% %arg2% %arg3%
python ./src/line_block.py %arg1% %arg2% %arg3%
goto exit_p

:dot_block
set /p arg1=请输入点大小（默认3）：
set /p arg2=请输入密度缩放大小（默认0.1，越大越密）：
set /p arg3=请输入块大小（默认48）：
set /p arg4=请输入最小点密度（默认0.1，小于不显示）：
if "%arg1%"=="" set arg1=3
if "%arg2%"=="" set arg2=0.1
if "%arg3%"=="" set arg3=48
if "%arg4%"=="" set arg4=0.1
echo 参数 %arg1% %arg2% %arg3% %arg4%
python ./src/dot_block.py %arg1% %arg2% %arg3% %arg4%
goto exit_p

:combine
set /p arg1=[Y/N]是否合并点图，为否时合并线条图（默认否）：
if "%arg1%"=="" set arg1=N
if %arg1%==n set arg1=N
if %arg1%==y set arg1=Y
if %arg1%==Y goto continue_y
if %arg1%==N (goto continue_n) else (goto combine)
:continue_y
echo 合并点图
goto continue
:continue_n
echo 合并线条图
:continue
python ./src/combine.py %arg1%

:exit_p
pause
deactivate & exit
