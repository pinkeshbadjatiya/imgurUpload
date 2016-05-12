#!/bin/bash

if [ ! -d ~/bin ]
  mkdir ~/bin
fi
echo 'export PATH=$PATH:~/bin' >> ~/.bashrc
cp imgurUpload _imgur_upload.py ~/bin/
chmod +x ~/bin/imgurUpload ~/bin/_imgur_upload.py


