@echo off

echo ѡ�������
echo [0]�˳���[1]�߸壻[2]ƽ������ͼ��[3]��ͼ��[4]�ϲ�ͼƬ
set /p op=�����������ţ�

if %op%==0 exit

call ./.venv/Scripts/activate.bat

if %op%==1 goto edge
if %op%==2 goto line_block
if %op%==3 goto dot_block
if %op%==4 goto combine

:edge
set /p arg1=������������ϸ��Ĭ��5����
set /p arg2=�������˲���С��Ĭ��7����
if "%arg1%"=="" set arg1=5
if "%arg2%"=="" set arg2=7
echo ���� %arg1% %arg2%
python ./src/edge.py %arg1% %arg2%
goto exit_p

:line_block
set /p arg1=������������ϸ��Ĭ��2����
set /p arg2=�������ܶ����Ŵ�С��Ĭ��0.1��Խ��Խ�ܣ���
set /p arg3=��������С��Ĭ��48����
if "%arg1%"=="" set arg1=2
if "%arg2%"=="" set arg2=0.1
if "%arg3%"=="" set arg3=48
echo ���� %arg1% %arg2% %arg3%
python ./src/line_block.py %arg1% %arg2% %arg3%
goto exit_p

:dot_block
set /p arg1=��������С��Ĭ��3����
set /p arg2=�������ܶ����Ŵ�С��Ĭ��0.1��Խ��Խ�ܣ���
set /p arg3=��������С��Ĭ��48����
set /p arg4=��������С���ܶȣ�Ĭ��0.1��С�ڲ���ʾ����
if "%arg1%"=="" set arg1=3
if "%arg2%"=="" set arg2=0.1
if "%arg3%"=="" set arg3=48
if "%arg4%"=="" set arg4=0.1
echo ���� %arg1% %arg2% %arg3% %arg4%
python ./src/dot_block.py %arg1% %arg2% %arg3% %arg4%
goto exit_p

:combine
set /p arg1=[Y/N]�Ƿ�ϲ���ͼ��Ϊ��ʱ�ϲ�����ͼ��Ĭ�Ϸ񣩣�
if "%arg1%"=="" set arg1=N
if %arg1%==n set arg1=N
if %arg1%==y set arg1=Y
if %arg1%==Y goto continue_y
if %arg1%==N (goto continue_n) else (goto combine)
:continue_y
echo �ϲ���ͼ
goto continue
:continue_n
echo �ϲ�����ͼ
:continue
python ./src/combine.py %arg1%

:exit_p
pause
deactivate & exit
