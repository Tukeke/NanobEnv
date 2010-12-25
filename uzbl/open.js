var o = '%s';
if(o.indexOf('.') > 0){
    if(o.indexOf(':') < 0) o = 'http://' + o
    window.location = o;
} else window.location = 'https://ssl.scroogle.org/cgi-bin/nbbwssl.cgi?Gw=' + o
