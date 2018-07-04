var instapaper=function (){var d=document,z=d.createElement('scr'+'ipt'),b=d.body,l=d.location;try{if(!b)throw(0);d.title='(Saving...) '+d.title;z.setAttribute('src',l.protocol+'//www.instapaper.com/j/Qn6obEE5qPiT?a=read-later&u='+encodeURIComponent(l.href)+'&t='+(new Date().getTime()));b.appendChild(z);}catch(e){alert('Please wait until the page has loaded.');}};

var facebook=function(){location.href='http://www.facebook.com/sharer.php?src=bm&v=4&i=1301235609&u='+encodeURIComponent(window.location.href)+'&t='+encodeURIComponent(document.title)};

var archive=function(){location.href='https://archive.is/?run=1&url='+encodeURIComponent(window.location.href)+'&t='+encodeURIComponent(document.title)};
var getArchive=function(){location.href='https://archive.is/'+window.location.href};

var mkpwd = {
    pwdElement:[],
    getClearPwd: function() {
        // search for password input elements and return first one value
        e = document.querySelectorAll('input[type="password"]');
        this.pwdElement = e;
        return this.pwdElement[0].value;
    },
    setCryptPwd: function(pwd) {
        var k; 
        if(this.pwdElement){
            //console.log(pwd);
            for(k=0; k<this.pwdElement.length; k++) 
                this.pwdElement[k].value=pwd;
        }
    },
    get: function() {
        if(this.pwdElement[0]){
            return this.pwdElement[0].value;
        }else{
            return false
        }
    }
}

// Converts the bookmarkfile under $XDG_CONFIG_HOME/vimb/bookmark into nice html.
// This script should be put into scripts.js file in vimb's config directory.
// Open vimb's bookmark file in vimb file:///home/{user}/.config/vimb/bookmark and
// run ':e! bookmarkFileToHtml();'
// Or start the pretty view by autocmd in cofig file like
//
// autocmd LoadFinished file:///*/bookmark e! bookmarkFileToHtml();
function bookmarkFileToHtml() {
    var parts=[], i, line, uri, lines = document.body.innerText.split(/\n/),
        html  = "<tr><th>Bookmark</th><th>Tag(s)</th></tr>",
        head  = '<head><style type="text/css">'
            + "body{background:#e0ddda}"
            + "table{margin:.5em auto;max-width:60em;border-collapse:collapse;color:#fff;}"
            + "th{text-align:left;background:#555;color:white;border-bottom:.3em solid #e0ddda;padding:14px 12px}"
            + "label{text-align:left;background:#555;color:white;}"
            + "td{padding:8px 12px;border-bottom:1px solid #e0ddda;color:#555}"
            + "pre{display:inline;margin-right:20px;color:#555:background-color:#fff}"
            + "tr{background:#fff}"
            + "div{margin:.5em auto;max-width:60em;border-collapse:collapse;color:#fff;background:#555}"
            + "</style></head>";

    for (i = 0; i < lines.length; i++) {
        line  = lines[i];
        if (!line) {
            continue;
        }
        parts = line.split("\t");
        uri   = parts[0];
        title = parts[1]||uri;
        tags  = (parts[2]||"").split(' ').sort().join(', ');
        html  = html + "<tr><td><a href=\"" + uri + "\">" + title + "</a></td><td>" + tags + "</td></tr>";
    }

	htmlHelp = "<div><pre>,,a</pre><label>To add page to archive.is + bookmark with tag archive</label><br><pre>,;a</pre><label>To get the current url from archive.is</label></div>"
    html = "<html>" + head + "<body>" + htmlHelp + "<table>" + html + "</table></body></html>";
    document.body.innerHTML = html;
}

function printGistPage() {
    var el=document.createElement('style');
    var fontSize='18px';
    el.media='print';
    el.innerHTML='#Header,#user-content-toc,.file-header,.gist-banner, .gistheader,.pagehead.repohead,.gist-description.container,.file-box .meta,#comments,.js-comment-form,#footer{display:none;}.file-box,file{border:0!important;}.markdown-body{font-size:'+fontSize+'}';
    document.getElementsByTagName('head')[0].appendChild(el);
}
