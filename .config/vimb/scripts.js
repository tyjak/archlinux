var instapaper=function (){var d=document,z=d.createElement('scr'+'ipt'),b=d.body,l=d.location;try{if(!b)throw(0);d.title='(Saving...) '+d.title;z.setAttribute('src',l.protocol+'//www.instapaper.com/j/Qn6obEE5qPiT?a=read-later&u='+encodeURIComponent(l.href)+'&t='+(new Date().getTime()));b.appendChild(z);}catch(e){alert('Please wait until the page has loaded.');}};

var facebook=function(){location.href='http://www.facebook.com/sharer.php?src=bm&v=4&i=1301235609&u='+encodeURIComponent(window.location.href)+'&t='+encodeURIComponent(document.title)};

var archive=function(){location.href='https://archive.is/?run=1&url='+encodeURIComponent(window.location.href)+'&t='+encodeURIComponent(document.title)};
var getArchive=function(){location.href='https://archive.is/'+window.location.href};

var read=function(){simplyread();}

var trelloNumber=function(){var n=$(".card-label.mod-card-front"); n.css({"padding":"0 6px","height":"16px","line-height":"16px","text-align":"center"}); var o=$(".card-short-id");o.each(function(){$(this).text($(this).text().replace("#","").replace("#","").replace("N.%C2%BA ", ""))});o.hasClass("hide")?o.removeClass("hide").css({"font-weight":"bold","font-size":".8em","margin-right":"5px",padding:"2.3px 6px","background":"#d6daDC","border-radius":"10px","color":"#4D4D4D"}):o.addClass("hide")};

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
var cssStyle = '<style type="text/css">'
            + "body{background:#002b36; color:#859000}"
            + "a:link{color:#fdf6e3; text-decoration:none}"
            + "a:visited{color:#93a1a1}"
            + "a:hover{color:#b58900}"
            + "table{margin:.5em auto;max-width:60em;border-collapse:collapse;color:#fdf6e3;}"
            + "th{text-align:left;background:#859900;color:#fdf6e3;border-bottom:.3em solid #073642;padding:14px 12px}"
            + "label{text-align:left;background:#859900;color:#fdf6e3;}"
            + "td{padding:8px 12px;border-bottom:1px solid #073642;color:#859900; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 100ch;}"
            + "pre{display:inline;margin-right:20px;color:#859000:background-color:#fdf6e3}"
            + "tr{background:#002b36}"
            + "div{margin:.5em auto;max-width:60em;border-collapse:collapse;color:#002b36;background:#859000}"
            + "</style>";

function bookmarkFileToHtml() {
    var parts=[], i, line, uri, lines = document.body.innerText.split(/\n/),
        html  = "<tr><th>Bookmark</th><th>Tag(s)</th></tr>",
        head  = '<head>'
            + cssStyle
            + "</head>";

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
function linkFileToHtml(title) {
    var parts=[], i, line, uri, lines = Array.from(new Set(document.body.innerText.split(/\n/).reverse())),
        html  = "<tr><th>" + title + "</th></tr>",
        head  = '<head><title>' + title + '</title>'
            + cssStyle
            + "</head>";

    for (i = 0; i < lines.length; i++) {
        line  = lines[i];
        if (!line) {
            continue;
        }
        parts = line.split("\t");
        uri   = parts[0];
        title = parts[1]||uri;
        html  = html + "<tr><td><a href=\"" + uri + "\">" + title + "</a></td></tr>";
    }

    htmlHead = "<span><a href=\"file:////home/david/.config/vimb/bookmark\">Bookmark</a> - <a href=\"file:////home/david/.config/vimb/history\">Historique</a> - <a href=\"file:////home/david/.config/vimb/closed\">Derniers onglets ouverts</a> - <a href=\"https://fanglingsu.github.io/vimb/man.html\">Aide</a></span>"
    html = "<html>" + head + "<body>" + htmlHead + "<table>" + html + "</table></body></html>";
    document.body.innerHTML = html;
}

// simplyread

/* See COPYING file for copyright, license and warranty details. */

if(window.content && window.content.document && window.content.document.simplyread_original === undefined) window.content.document.simplyread_original = false;

function simplyread(nostyle, nolinks)
{
	/* count the number of <p> tags that are direct children of parenttag */
	function count_p(parenttag)
	{
		var n = 0;
		var c = parenttag.childNodes;
		for (var i = 0; i < c.length; i++) {
			if (c[i].tagName == "p" || c[i].tagName == "P")
				n++;
		}
		return n;
	}
	
	var doc;
	doc = (document.body === undefined)
	      ? window.content.document : document;
	
	/* if simplyread_original is set, then the simplyread version is currently active,
	 * so switch to the simplyread_original html */
	if (doc.simplyread_original) {
		doc.body.innerHTML = doc.simplyread_original;
		for (var i = 0; i < doc.styleSheets.length; i++)
			doc.styleSheets[i].disabled = false;
		doc.simplyread_original = false
		return 0;
	}
	
	doc.simplyread_original = doc.body.innerHTML;
	doc.body.innerHTML = doc.body.innerHTML.replace(/<br[^>]*>\s*<br[^>]*>/g, "<p>");
	
	var biggest_num = 0;
	var biggest_tag;
	
	/* search for tag with most direct children <p> tags */
	var t = doc.getElementsByTagName("*");
	for (var i = 0; i < t.length; i++) {
		var p_num = count_p(t[i]);
		if (p_num > biggest_num) {
			biggest_num = p_num;
			biggest_tag = t[i];
		}
	}
	
	if (biggest_num == 0) return 1;
	
	/* save and sanitise content of chosen tag */
	var fresh = doc.createElement("div");
	fresh.innerHTML = biggest_tag.innerHTML;
	fresh.innerHTML = fresh.innerHTML.replace(/<\/?font[^>]*>/g, "");
	fresh.innerHTML = fresh.innerHTML.replace(/style="[^"]*"/g, "");
	if(nolinks)
		fresh.innerHTML = fresh.innerHTML.replace(/<\/?a[^>]*>/g, "");
	fresh.innerHTML = fresh.innerHTML.replace(/<\/?span[^>]*>/g, "");
	fresh.innerHTML = fresh.innerHTML.replace(/<style[^>]*>/g, "<style media=\"aural\">"); /* ensures contents of style tag are ignored */
	
	for (var i = 0; i < doc.styleSheets.length; i++)
		doc.styleSheets[i].disabled = true;
	
	srstyle =
		"p{margin:0ex auto;} h1,h2,h3,h4{font-weight:normal}" +
		"p+p{text-indent:2em;} body{background:#cccccc none}" +
		"img{display:block; max-width: 32em; padding:1em; margin: auto}" +
		"h1{text-align:center;text-transform:uppercase}" +
		"div#sr{width:34em; padding:8em; padding-top:2em;" +
		"  background-color:white; margin:auto; line-height:1.4;" +
		"  text-align:justify; font-family:serif; hyphens:auto;}";
		/* text-rendering:optimizeLegibility; - someday this will work,
		 *   but at present it just ruins justify, so is disabled */
	
	doc.body.innerHTML =
		"<style type=\"text/css\">" + (nostyle ? "" : srstyle) + "</style>" +
		"<div id=\"sr\">" + "<h1>"+doc.title+"</h1>" + fresh.innerHTML + "</div>";
	
	return 0;
}

//TO FIX
function checkHtml()
{
    var _p='//squizlabs.github.io/HTML_CodeSniffer/build/';
    var _i=function(s,cb) {
        var sc=document.createElement('script');
        sc.onload = function() {
            sc.onload = null;
            sc.onreadystatechange = null;
            cb.call(this);
        };
        sc.onreadystatechange = function(){
            if(/^(complete|loaded)$/.test(this.readyState) === true){
                sc.onreadystatechange = null;sc.onload();
            }
        };
        sc.src=s;
        if (document.head) {
            document.head.appendChild(sc);
        } else {
            document.getElementsByTagName('head')[0].appendChild(sc);
        }
    };
    var options={path:_p};
    _i(_p+'HTMLCS.js',function(){HTMLCSAuditor.run('WCAG2AA',null,options);});
}
