call conda create -n FLAME python=3.8
call conda activate FLAME

@REM v2.1.0
call conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

pip install pyrender smplx chumpy
pip install numpy==1.23.4
