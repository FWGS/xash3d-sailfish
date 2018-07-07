This repository intended to store all dependencies(as submodules) and *.spec file for Sailfish OS.

How to build: 

0. ```git clone```

1. ```git submodules update --init --recursive```

2. Run Sailfish OS SDK virtual machine.

3. Navigate to the root of this repo.

4. ```mb2 -t $TOOLCHAIN_NAME build```

How to use:

Run in console:

```XASH3D_BASEDIR=/home/nemo/xash LD_LIBRARY_PATH=/usr/lib/xash3d /usr/lib/xash3d/xash3d```

Found a bug? Send it to github.com/FWGS/xash3d. 
