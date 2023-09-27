url=https://www.unibet.fr/sport/football/ligue-1-ubereats
// content might be displayed via some javascript which I am unable to get from Curl 

urll=https://www.chat-et-chaton.com/elevage/france/occitanie-76.html

curl -i $url \
-o request \
--compressed \
-H "Referer: https://www.google.com/" \
-H "Connection: keep-alive" \
-H "Cache-Control: max-age=0" \
-H "Upgrade-Insecure-Requests: 1" \
-H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36" \
-H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" \
-H "Sec-Fetch-Site: none" \
-H "Sec-Fetch-Mode: navigate" \
-H "Sec-Fetch-User: ?1" \
-H "Sec-Fetch-Dest: document" \
-H "Accept-Encoding: gzip, deflate, br" \
-H "Accept-Language: fr;q=0.9" \
