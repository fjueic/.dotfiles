selected_text=$(cliphist list | head -n 20 | rofi -dmenu)
  if [ -n "$selected_text" ]; then
    echo "$selected_text" | cliphist decode | wl-copy
  fi
