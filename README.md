Note:- Incomplete

### These are my configurations files for my arch linux system.

### Essintial packages
```bash
sudo pacman -S git
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd .. && rm -rf paru
paru -S git neovim tmux node npm ripgrep unzip wget curl
```

### Window Manager
```bash
paru -S hyprland hyprlpaper hyprlock hypridle dunst waybar python-watchdog foot rofi libnotify upower pavucontrol wl-clipboard cliphist imagemagick firefox-developer-edition mpvpaper hyprpicker brightnessctl pamixer playerctl wayvnc polkit-kde-agent gnome-keyring network-manager-applet networkmanager kdeconnect syncthing slurp grim python-pyudev`
```

### Bluetooth
```bash
paru -S bluez bluez-utils blueman 
sudo systemctl start bluetooth.service
sudo systemctl enable bluetooth.service
```
###  Screenshots

# ![Screenshot](https://i.imgur.com/atcFeOF.png)
# ![Screenshot](https://i.imgur.com/EtR557q.png)
# ![Screenshot](https://i.imgur.com/615wOqQ.png)
# ![Screenshot](https://i.imgur.com/ySJSTv7.png)
