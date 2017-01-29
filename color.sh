cp GVN.html GVN_colored.html
python3 add_highlights.py --color "rgb(234, 255, 234)" --filename GVN_colored.html "$(cat green)"
python3 add_highlights.py --color "rgb(248, 238, 199)" --filename GVN_colored.html "$(cat yellow)"
