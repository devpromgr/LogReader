directory="$1"
size="$2"

# Use find and truncate to recursively truncate files
# find "$directory" -type f -exec truncate -s "$size" {} \;
find logDeviceTypesVerySmall -type f -exec truncate -s 2000 {} \;