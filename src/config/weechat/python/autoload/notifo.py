  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>weechat-plugins/python/notifo.py at master · norrs/weechat-plugins · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon-precomposed" sizes="57x57" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="apple-touch-icon-144.png" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="7g+R4wMhgOFnVGIK/OtwofW41VjBrfnTXRrNDQyZoKs=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-407693f9f73c33bc72d72bf9656fbf5ae05597d3.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-56ff2781ae95d3a31c723b6774df51dd407ef091.css" media="screen" rel="stylesheet" type="text/css" />
    


        <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-d61440caec5d2210a2242b084cdb2bc6597e00b7.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-3caac5eb6f4ff7cdd70b7b145f68d0e4cc0f9a28.js" type="text/javascript"></script>
      

        <link rel='permalink' href='/norrs/weechat-plugins/blob/f5b72c180c8dc6ca2387785d53110b62987033f4/python/notifo.py'>
    <meta property="og:title" content="weechat-plugins"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/norrs/weechat-plugins"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/6cbdf33a7182328773455cb0638dfec0?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="Contribute to weechat-plugins development by creating an account on GitHub."/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="norrs/weechat-plugins"/>

    <meta name="description" content="Contribute to weechat-plugins development by creating an account on GitHub." />

  <link href="https://github.com/norrs/weechat-plugins/commits/master.atom" rel="alternate" title="Recent Commits to weechat-plugins:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production  ">
    <div id="wrapper">

      

      

      

      


        <div class="header header-logged-out">
          <div class="container clearfix">

            <a class="header-logo-wordmark" href="https://github.com/">
              <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1338956357" />
              <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1338956357" />
            </a>

              
<ul class="top-nav">
    <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
  <li class="search"><a href="https://github.com/search">Search</a></li>
  <li class="features"><a href="https://github.com/features">Features</a></li>
    <li class="blog"><a href="https://github.com/blog">Blog</a></li>
</ul>


            <div class="header-actions">
                <a class="button primary" href="https://github.com/signup">Sign up for free</a>
              <a class="button" href="https://github.com/login?return_to=%2Fnorrs%2Fweechat-plugins%2Fblob%2Fmaster%2Fpython%2Fnotifo.py">Sign in</a>
            </div>

          </div>
        </div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu">
          <div class="container">
            <div class="title-actions-bar">
              


<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2Fnorrs%2Fweechat-plugins"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="mini-icon mini-icon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/norrs/weechat-plugins/stargazers">
        0
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fnorrs%2Fweechat-plugins"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="mini-icon mini-icon-fork"></span>Fork
      </a>
      <a href="/norrs/weechat-plugins/network" class="social-count">
        0
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/norrs" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">norrs</span>
                  </a></span> /
                <strong><a href="/norrs/weechat-plugins" class="js-current-repository">weechat-plugins</a></strong>
              </h1>
            </div>

            

  <ul class="tabs">
    <li><a href="/norrs/weechat-plugins" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/norrs/weechat-plugins/network" highlight="repo_network">Network</a></li>
    <li><a href="/norrs/weechat-plugins/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/norrs/weechat-plugins/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>



    <li><a href="/norrs/weechat-plugins/graphs" highlight="repo_graphsrepo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/norrs/weechat-plugins/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="mini-icon mini-icon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container js-select-menu-pane">

        <div class="select-menu-modal js-select-menu-pane">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-select-menu-text-filter js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div> <!-- /.select-menu-text-filter -->
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-filter="branches" class="js-select-menu-tab selected">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list js-filter-tab js-filter-branches css-truncate" data-filterable-for="commitish-filter-field" data-filterable-type="substring">



              <div class="select-menu-item js-navigation-item js-navigation-target ">
                <span class="select-menu-checkmark mini-icon mini-icon-confirm"></span>
                <a href="/norrs/weechat-plugins/blob/automode-check-operatorstatus/python/notifo.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="automode-check-operatorstatus" rel="nofollow" title="automode-check-operatorstatus">automode-check-operatorstatus</a>
              </div> <!-- /.select-menu-item -->

              <div class="select-menu-item js-navigation-item js-navigation-target selected">
                <span class="select-menu-checkmark mini-icon mini-icon-confirm"></span>
                <a href="/norrs/weechat-plugins/blob/master/python/notifo.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
              </div> <!-- /.select-menu-item -->

              <div class="select-menu-no-results js-not-filterable">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list js-filter-tab js-filter-tags css-truncate" data-filterable-for="commitish-filter-field" data-filterable-type="substring" style="display:none;">


            <div class="select-menu-no-results js-not-filterable">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/norrs/weechat-plugins" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/norrs/weechat-plugins/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/norrs/weechat-plugins/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">2</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:7bae788e1051e45251e0198f1e30f18c -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:7bae788e1051e45251e0198f1e30f18c -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/norrs/weechat-plugins" class="js-slide-to" data-direction="back" itemscope="url"><span itemprop="title">weechat-plugins</span></a></span></span> / <span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/norrs/weechat-plugins/tree/master/python" class="js-slide-to" data-direction="back" itemscope="url"><span itemprop="title">python</span></a></span> / <strong class="final-path">notifo.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="python/notifo.py" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
        </div>

      <a href="/norrs/weechat-plugins/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/7e5f6d6e2a4a1d05690d0550eb832c20?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/flashcode" rel="author">flashcode</a></span>
    <time class="js-relative-date" datetime="2011-09-17T12:38:12-07:00" title="2011-09-17 12:38:12">September 17, 2011</time>
    <div class="commit-title">
        <a href="/norrs/weechat-plugins/commit/c85eb9b072bce4f3ada8d3e83548fdd4dd4dec22" class="message">New script notifo.py: send push notifications to your iPhone/Android …</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/7e5f6d6e2a4a1d05690d0550eb832c20?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/flashcode">flashcode</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/norrs/weechat-plugins/blob/f5b72c180c8dc6ca2387785d53110b62987033f4/python/notifo.py" data-title="weechat-plugins/python/notifo.py at master · norrs/weechat-plugins · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>75 lines (62 sloc)</span>
                <span>2.975 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/norrs/weechat-plugins/raw/master/python/notifo.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/norrs/weechat-plugins/blame/master/python/notifo.py" class="button minibutton ">Blame</a>
                  <a href="/norrs/weechat-plugins/commits/master/python/notifo.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="data type-python js-blob-data">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
</pre>
          </td>
          <td width="100%">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c"># Author: ochameau &lt;poirot.alex AT gmail DOT com&gt;</span></div><div class='line' id='LC2'><span class="c"># Homepage: https://github.com/ochameau/weechat-notifo</span></div><div class='line' id='LC3'><span class="c"># Derived from: notify</span></div><div class='line' id='LC4'><span class="c">#   Author: lavaramano &lt;lavaramano AT gmail DOT com&gt;</span></div><div class='line' id='LC5'><span class="c">#   Improved by: BaSh - &lt;bash.lnx AT gmail DOT com&gt;</span></div><div class='line' id='LC6'><span class="c">#   Ported to Weechat 0.3.0 by: Sharn - &lt;sharntehnub AT gmail DOT com)</span></div><div class='line' id='LC7'><span class="c"># And from: notifo_notify</span></div><div class='line' id='LC8'><span class="c">#   Author: SAEKI Yoshiyasu &lt;laclef_yoshiyasu@yahoo.co.jp&gt;</span></div><div class='line' id='LC9'><span class="c">#   Homepage: http://bitbucket.org/laclefyoshi/weechat/</span></div><div class='line' id='LC10'><span class="c"># This plugin send push notifications to your iPhone or Android smartphone</span></div><div class='line' id='LC11'><span class="c"># by using Notifo.com mobile application/services</span></div><div class='line' id='LC12'><span class="c"># Requires Weechat 0.3.0</span></div><div class='line' id='LC13'><span class="c"># Released under GNU GPL v2</span></div><div class='line' id='LC14'><span class="c">#</span></div><div class='line' id='LC15'><span class="c"># 2011-08-27, ochameau &lt;poirot.alex@gmail.com&gt;:</span></div><div class='line' id='LC16'><span class="c">#     version 0.1: merge notify.py and notifo_notify.py in order to avoid</span></div><div class='line' id='LC17'><span class="c">#                  sending notifications when channel or private buffer is</span></div><div class='line' id='LC18'><span class="c">#                  already opened</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="kn">import</span> <span class="nn">weechat</span><span class="o">,</span> <span class="nn">string</span><span class="o">,</span> <span class="nn">urllib</span><span class="o">,</span> <span class="nn">urllib2</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="n">weechat</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="s">&quot;notifo&quot;</span><span class="p">,</span> <span class="s">&quot;ochameau&quot;</span><span class="p">,</span> <span class="s">&quot;0.1&quot;</span><span class="p">,</span> <span class="s">&quot;GPL&quot;</span><span class="p">,</span> <span class="s">&quot;notifo: Send push notifications to your iPhone/Android about your private messages and highlights.&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="n">credentials</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;username&quot;</span><span class="p">:</span> <span class="s">&quot;&quot;</span><span class="p">,</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;api_secret&quot;</span><span class="p">:</span> <span class="s">&quot;&quot;</span></div><div class='line' id='LC27'><span class="p">}</span></div><div class='line' id='LC28'><br/></div><div class='line' id='LC29'><span class="k">for</span> <span class="n">option</span><span class="p">,</span> <span class="n">default_value</span> <span class="ow">in</span> <span class="n">credentials</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">weechat</span><span class="o">.</span><span class="n">config_get_plugin</span><span class="p">(</span><span class="n">option</span><span class="p">)</span> <span class="o">==</span> <span class="s">&quot;&quot;</span><span class="p">:</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">weechat</span><span class="o">.</span><span class="n">prnt</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">weechat</span><span class="o">.</span><span class="n">prefix</span><span class="p">(</span><span class="s">&quot;error&quot;</span><span class="p">)</span> <span class="o">+</span> <span class="s">&quot;notifo: Please set option: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">option</span><span class="p">)</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">weechat</span><span class="o">.</span><span class="n">prnt</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="s">&quot;notifo: /set plugins.var.python.notifo.</span><span class="si">%s</span><span class="s"> STRING&quot;</span> <span class="o">%</span> <span class="n">option</span><span class="p">)</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'><span class="c"># Hook privmsg/hilights</span></div><div class='line' id='LC35'><span class="n">weechat</span><span class="o">.</span><span class="n">hook_print</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="s">&quot;irc_privmsg&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="s">&quot;notify_show&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="c"># Functions</span></div><div class='line' id='LC38'><span class="k">def</span> <span class="nf">notify_show</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">bufferp</span><span class="p">,</span> <span class="n">uber_empty</span><span class="p">,</span> <span class="n">tagsn</span><span class="p">,</span> <span class="n">isdisplayed</span><span class="p">,</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ishilight</span><span class="p">,</span> <span class="n">prefix</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">bufferp</span> <span class="o">==</span> <span class="n">weechat</span><span class="o">.</span><span class="n">current_buffer</span><span class="p">()):</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">weechat</span><span class="o">.</span><span class="n">buffer_get_string</span><span class="p">(</span><span class="n">bufferp</span><span class="p">,</span> <span class="s">&quot;localvar_type&quot;</span><span class="p">)</span> <span class="o">==</span> <span class="s">&quot;private&quot;</span><span class="p">:</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">show_notification</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">ishilight</span> <span class="o">==</span> <span class="s">&quot;1&quot;</span><span class="p">:</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">buffer</span> <span class="o">=</span> <span class="p">(</span><span class="n">weechat</span><span class="o">.</span><span class="n">buffer_get_string</span><span class="p">(</span><span class="n">bufferp</span><span class="p">,</span> <span class="s">&quot;short_name&quot;</span><span class="p">)</span> <span class="ow">or</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">weechat</span><span class="o">.</span><span class="n">buffer_get_string</span><span class="p">(</span><span class="n">bufferp</span><span class="p">,</span> <span class="s">&quot;name&quot;</span><span class="p">))</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">show_notification</span><span class="p">(</span><span class="nb">buffer</span><span class="p">,</span> <span class="n">prefix</span> <span class="o">+</span> <span class="s">&quot;: &quot;</span> <span class="o">+</span> <span class="n">message</span><span class="p">)</span></div><div class='line' id='LC51'><br/></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">weechat</span><span class="o">.</span><span class="n">WEECHAT_RC_OK</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'><span class="k">def</span> <span class="nf">show_notification</span><span class="p">(</span><span class="n">chan</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">NOTIFO_USER</span> <span class="o">=</span> <span class="n">weechat</span><span class="o">.</span><span class="n">config_get_plugin</span><span class="p">(</span><span class="s">&quot;username&quot;</span><span class="p">)</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">NOTIFO_API_SECRET</span> <span class="o">=</span> <span class="n">weechat</span><span class="o">.</span><span class="n">config_get_plugin</span><span class="p">(</span><span class="s">&quot;api_secret&quot;</span><span class="p">)</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">NOTIFO_USER</span> <span class="o">!=</span> <span class="s">&quot;&quot;</span> <span class="ow">and</span> <span class="n">NOTIFO_API_SECRET</span> <span class="o">!=</span> <span class="s">&quot;&quot;</span><span class="p">:</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">url</span> <span class="o">=</span> <span class="s">&quot;https://api.notifo.com/v1/send_notification&quot;</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">opt_dict</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;msg&quot;</span><span class="p">:</span> <span class="n">message</span><span class="p">,</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;label&quot;</span><span class="p">:</span> <span class="s">&quot;weechat&quot;</span><span class="p">,</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;title&quot;</span><span class="p">:</span> <span class="n">chan</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">opt</span> <span class="o">=</span> <span class="n">urllib</span><span class="o">.</span><span class="n">urlencode</span><span class="p">(</span><span class="n">opt_dict</span><span class="p">)</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">basic</span> <span class="o">=</span> <span class="s">&quot;Basic </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="s">&quot;:&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">NOTIFO_USER</span><span class="p">,</span> <span class="n">NOTIFO_API_SECRET</span><span class="p">])</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&quot;base64&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">python2_bin</span> <span class="o">=</span> <span class="n">weechat</span><span class="o">.</span><span class="n">info_get</span><span class="p">(</span><span class="s">&quot;python2_bin&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span> <span class="ow">or</span> <span class="s">&quot;python&quot;</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">weechat</span><span class="o">.</span><span class="n">hook_process</span><span class="p">(</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">python2_bin</span> <span class="o">+</span> <span class="s">&quot; -c </span><span class="se">\&quot;</span><span class="s">import urllib2</span><span class="se">\n</span><span class="s">&quot;</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;req = urllib2.Request(&#39;&quot;</span> <span class="o">+</span> <span class="n">url</span> <span class="o">+</span> <span class="s">&quot;&#39;, &#39;&quot;</span> <span class="o">+</span> <span class="n">opt</span> <span class="o">+</span> <span class="s">&quot;&#39;)</span><span class="se">\n</span><span class="s">&quot;</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;req.add_header(&#39;Authorization&#39;, &#39;&quot;</span> <span class="o">+</span> <span class="n">basic</span> <span class="o">+</span> <span class="s">&quot;&#39;)</span><span class="se">\n</span><span class="s">&quot;</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;res = urllib2.urlopen(req)</span><span class="se">\n\&quot;</span><span class="s">&quot;</span><span class="p">,</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="mi">30</span> <span class="o">*</span> <span class="mi">1000</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'><span class="c"># vim: autoindent expandtab smarttab shiftwidth=4</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1347543528" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.04067s from fe1.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/norrs/weechat-plugins/suggestions/commit/f5b72c180c8dc6ca2387785d53110b62987033f4">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-icon mega-icon-normalscreen"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="mini-icon mini-icon-brightness"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.04114' data-host='fe1'></span>
    
  </body>
</html>

