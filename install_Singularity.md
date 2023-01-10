# Install Singularity

Instructions are based on [this guide](https://singularity-tutorial.github.io/01-installation/).

1. Install prerequisites

   ```sh
   sudo apt update && sudo apt-get install -y build-essential libseccomp-dev \
   pkg-config squashfs-tools cryptsetup curl wget git golang-go
   ```

<!-- 2. Install GO

   ```sh
   wget https://dl.google.com/go/go1.13.linux-amd64.tar.gz 
   sudo tar --directory=/usr/local -xzvf go1.13.linux-amd64.tar.gz
   export PATH=/usr/local/go/bin:$PATH
   rm go1.13.linux-amd64.tar.gz
   ``` -->

   <!-- **Reload the shell** by typing in `bash` or `zsh`, based on your shell. -->

2. Download Singularity

   ```sh
   git clone --recurse-submodules https://github.com/sylabs/singularity.git ~/singularity
   ```

4. Install Singularity

   ```sh
   cd ~/singularity
   ./mconfig
   cd builddir
   make
   sudo make install
   ```