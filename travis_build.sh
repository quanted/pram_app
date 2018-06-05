#!/bin/sh
git clone https://github.com/quanted/requirements_qed.git

for package in $(cat requirements_qed/requirements.txt)
do
    if [[ $package != #* ]] || [[ $package != *gdal* ]] || [[$package != *fiona* ]]; then
        pip install $package
done