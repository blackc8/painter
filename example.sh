source painter.sh
label "Tool Name"
desc "This tool is used to do so and so this.\nIt is easy fast and cool"
echo ''
Head "Sub heading name"
ask "Say something: " False True
scs "Checking message..."
blt "Checking grammer"
wrn "Your message seems to be gramatically wrong!"
printf " Your message: $bold$purple$inp$ncol\n"
err "Something went wrong!"
