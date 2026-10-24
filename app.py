import os, re, io, base64
import streamlit as st
from PIL import Image

# ================= EDIT ONLY THIS =================
D = {
    "first": "Sohail", "last": "Khan",
    "role": "Data Scientist",
    "tagline": "I build data products end to end: web scraping, SQL, statistics, machine learning and deployed Streamlit apps. Open to full-time data science roles.",
    "location": "Bhopal, India",
    "email": "sohail438216@gmail.com",
    "linkedin": "https://www.linkedin.com/in/sohail-khan73/",
    "github": "https://github.com/sohail73",
    "typed": "DATA SCIENCE · STATISTICS · MACHINE LEARNING",
    "stats": [("10", "Regression models compared"), ("3", "Recommender systems built"), ("AWS", "Project deployed end to end"), ("B.Tech", "CSE · Data Science")],
    "about_big": ("Hi, I'm", "Sohail."),
    "about": [
        "I am a Data Science student at Technocrats Institute of Technology, Bhopal, and I am looking for a full-time role where I can turn data into decisions.",
        "I enjoy the whole lifecycle: scraping and cleaning messy data, finding patterns with statistics and exploratory analysis, building machine learning models and shipping them as apps people can actually use.",
        "My capstone, a real estate price prediction and recommendation platform deployed on AWS, shows how I work: from raw listings to a live product.",
    ],
    "why": [
        ("I build end to end", "From scraping raw listings to a model deployed on AWS, I own every stage of the pipeline, not just the notebook."),
        ("I can explain my models", "I used feature selection, permutation importance and SHAP so predictions are interpretable, not a black box."),
        ("I ship usable products", "My Streamlit app combines price prediction, market analytics and a recommender that anyone can use."),
    ],
    "facts": [("Based in", "Bhopal, India"), ("Education", "B.Tech, CSE (Data Science)"), ("College", "Technocrats Institute of Technology, Bhopal"), ("Looking for", "Full-time data science roles"), ("Email", "sohail438216@gmail.com")],
    "project": {
        "tag": "Capstone · Machine Learning & Analytics",
        "name": "Real Estate Analytics & Price Prediction Platform",
        "summary": "An end-to-end data science application. I scraped property listings from 99acres, cleaned and engineered features, compared 10 regression models, and shipped a Streamlit app with price prediction, market analytics and a recommender system, deployed on AWS.",
        "github": "", "demo": "",
        "steps": [
            ("Data Gathering", "Self-scraped listings from 99acres and explored other property sites for a more diverse dataset."),
            ("Cleaning & Merging", "Handled missing values, standardised formats and merged houses and flats into one dataset."),
            ("Feature Engineering", "Created features such as luxury score, furnishing details, age of possession and area type."),
            ("Exploratory Analysis", "Univariate and multivariate analysis, supported by Pandas Profiling."),
            ("Outliers & Imputation", "Removed outliers and imputed missing values in key columns like area and bedrooms."),
            ("Feature Selection", "Correlation, random forest and gradient boosting importance, permutation importance, LASSO, RFE and SHAP."),
            ("Model Selection", "Compared 10 regression models and built a prediction pipeline with encoding."),
            ("Deployment", "Packaged as a Streamlit app and deployed on AWS."),
        ],
        "modules": [
            ("Price Predictor", "Interactive app that estimates property prices using the selected regression pipeline."),
            ("Analytics Module", "Geographical maps, amenity word clouds, scatter plots, pie charts and box plots of the market."),
            ("Recommender System", "Three recommendation models based on top facilities, price details and location advantages."),
        ],
        "models": ["Linear Regression", "SVR", "Random Forest", "MLP", "LASSO", "Ridge", "Gradient Boosting", "Decision Tree", "KNN", "ElasticNet"],
        "stack": ["Web Scraping", "Data Cleaning", "Feature Engineering", "EDA", "Pandas Profiling", "Feature Selection", "SHAP", "Regression Modeling", "Recommender Systems", "Data Visualization", "Streamlit", "AWS"],
    },
    "groups": {
        "Programming & Databases": ("🐍", "Write code, query and manage data", ["Python", "SQL", "MySQL"]),
        "Data Analysis": ("🐼", "Clean, transform and analyse data", ["Pandas", "NumPy", "Statistics"]),
        "Machine Learning": ("🤖", "Build and evaluate predictive models", ["Machine Learning"]),
        "Data Collection": ("🕸️", "Scrape and collect data from the web", ["Selenium", "Requests", "BeautifulSoup"]),
        "Data Visualization": ("📊", "Turn data into clear visuals", ["Plotly", "Matplotlib", "Seaborn", "Power BI", "Excel"]),
        "Apps & Version Control": ("🚀", "Deploy apps and track code", ["Streamlit", "Git", "GitHub"]),
    },
    "orbit": [
        (1, "icon", "python", "Python"), (1, "icon", "pandas", "Pandas"), (1, "icon", "numpy", "NumPy"), (1, "text", "ML", "Machine Learning"),
        (2, "text", "σ", "Statistics"), (2, "text", "SQL", "SQL"), (2, "icon", "mysql", "MySQL"),
        (2, "icon", "matplotlib", "Matplotlib"), (2, "text", "Sns", "Seaborn"), (2, "icon", "plotly", "Plotly"),
        (3, "icon", "selenium", "Selenium"), (3, "text", "BS4", "BeautifulSoup"), (3, "text", "Req", "Requests"),
        (3, "icon", "streamlit", "Streamlit"), (3, "icon", "git", "Git"), (3, "icon", "github", "GitHub"),
    ],
    "tools": ["Python", "NumPy", "Pandas", "SQL", "MySQL", "Statistics", "Machine Learning", "Selenium", "Requests", "BeautifulSoup", "Matplotlib", "Seaborn", "Plotly", "Streamlit", "Power BI", "Excel", "Git", "GitHub"],
}
# ==================================================


def photo_uri():
    for ext, mime in (("jpg", "jpeg"), ("jpeg", "jpeg"), ("png", "png"), ("webp", "webp")):
        p = f"profile.{ext}"
        if os.path.exists(p):
            with open(p, "rb") as f:
                return f"data:image/{mime};base64," + base64.b64encode(f.read()).decode()
    return None

def icon_uri(n):
    p = f"assets/{n}.svg"
    if os.path.exists(p):
        with open(p, "rb") as f:
            return "data:image/svg+xml;base64," + base64.b64encode(f.read()).decode()
    return None



FAVICON = "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"

st.set_page_config(page_title=f"{D['first']} {D['last']} | {D['role']}", page_icon=Image.open(io.BytesIO(base64.b64decode(FAVICON))), layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap');
@property --a {syntax:'<angle>'; inherits:false; initial-value:0deg;}
html,body,[class*="css"]{font-family:'Space Grotesk',sans-serif;}
#MainMenu,footer,header{visibility:hidden;}
.stApp{background:#030303;
 background-image:radial-gradient(900px 500px at 85% -5%,rgba(255,255,255,.07),transparent 60%),
 radial-gradient(700px 500px at -5% 30%,rgba(255,255,255,.04),transparent 60%),
 linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);
 background-size:auto,auto,56px 56px,56px 56px;}
.block-container{max-width:1500px;padding:1rem 3rem 2rem;}
html{scroll-behavior:smooth;}
.mono{font-family:'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;font-size:.72rem;color:#7A7A7A;}
.it{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;
 background:linear-gradient(90deg,#FFFFFF,#9A9A9A);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
@keyframes up{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:none}}
@keyframes spin{to{--a:360deg}}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(255,255,255,.6)}50%{box-shadow:0 0 0 8px rgba(255,255,255,0)}}
@keyframes marq{to{transform:translateX(-50%)}}
@keyframes type{from{width:0}to{width:100%}}
@keyframes blink{50%{border-color:transparent}}
.reveal{animation:up .9s cubic-bezier(.2,.7,.2,1) both;}
.nav{position:sticky;top:8px;z-index:99;display:flex;justify-content:space-between;align-items:center;padding:10px 12px 10px 22px;
 border-radius:99px;background:rgba(10,10,10,.7);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.08);margin-bottom:20px;}
.nav b{font-size:1.05rem}.nav a{color:#9A9A9A;text-decoration:none;margin:0 14px;font-size:.88rem;transition:.2s}.nav a:hover{color:#fff}
.nav .cta{background:#F2F2F2;color:#030303!important;padding:9px 20px;border-radius:99px;font-weight:600;margin:0}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:#E8E8E8;margin-right:10px;animation:pulse 2s infinite}
.hero{padding:70px 0 30px}
.hero h1{font-size:clamp(3.2rem,9vw,7rem);line-height:.95;font-weight:500;margin:18px 0;letter-spacing:-.03em}
.hero h1 .it{font-size:1.12em;padding-right:.1em}
.hero p{color:#9A9A9A;font-size:1.15rem;max-width:560px;line-height:1.7}
@keyframes reveal{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
.typed{display:inline-block;white-space:nowrap;animation:reveal 2.6s steps(36) .6s both}
.btn{display:inline-block;padding:14px 28px;border-radius:99px;font-weight:600;text-decoration:none!important;margin:22px 12px 0 0;transition:.3s}
.btn.p{background:#F2F2F2;color:#030303!important}
.btn.s{border:1px solid rgba(255,255,255,.2);color:#F2F2F2!important}
.btn:hover{transform:translateY(-3px);box-shadow:0 12px 40px rgba(255,255,255,.28)}
.orb{width:300px;height:300px;margin:auto;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:6.5rem;
 background:conic-gradient(from var(--a),#E8E8E8,#9A9A9A,#030303 40%,#E8E8E8);animation:spin 6s linear infinite;position:relative}
.orb:after{content:attr(data-i);position:absolute;inset:3px;border-radius:50%;background:#050505;display:flex;align-items:center;justify-content:center;font-family:'Instrument Serif',serif;font-style:italic;color:#F2F2F2}
.marq{overflow:hidden;border-block:1px solid rgba(255,255,255,.08);margin:50px 0;padding:16px 0;mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent)}
.marq div{display:flex;gap:48px;width:max-content;animation:marq 28s linear infinite}
.marq span{font-size:1.5rem;color:#5A5A5A;white-space:nowrap}.marq span:hover{color:#E8E8E8}
.stat{padding:26px 18px;border-left:1px solid rgba(255,255,255,.1)}
.stat h2{font-size:3rem;font-weight:500;margin:0;letter-spacing:-.03em}
.sec{margin:100px 0 10px}.sec h2{font-size:clamp(2.2rem,5vw,3.8rem);font-weight:500;line-height:1.05;margin:10px 0 0;letter-spacing:-.025em}
.sec h2 .it{font-size:1.1em}
.card{position:relative;padding:28px;border-radius:22px;height:100%;background:#0A0A0A;transition:.4s;
 border:1px solid transparent;background:linear-gradient(#0A0A0A,#0A0A0A) padding-box,conic-gradient(from var(--a),rgba(255,255,255,.08),rgba(255,255,255,.08) 70%,#E8E8E8,rgba(255,255,255,.08)) border-box;animation:spin 5s linear infinite}
.card:hover{transform:translateY(-8px);box-shadow:0 25px 60px rgba(255,255,255,.12)}
.card .n{font-size:.75rem;color:#E8E8E8}.card h3{font-size:1.45rem;margin:14px 0 8px;font-weight:500}
.card p{color:#8F8F8F;line-height:1.65;font-size:.95rem}
.imp{color:#E8E8E8;font-family:'JetBrains Mono';font-size:.8rem;margin:14px 0}
.chip{display:inline-block;padding:5px 12px;margin:4px 4px 0 0;border-radius:99px;font-size:.75rem;color:#CFCFCF;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08)}
.card a{color:#E8E8E8;text-decoration:none;font-size:.85rem;margin-right:16px}
.tl{display:grid;grid-template-columns:110px 1fr;gap:20px;padding:26px 0;border-top:1px solid rgba(255,255,255,.08)}
.tl h3{font-size:1.7rem;font-weight:500;margin:0 0 6px}.tl p{color:#8F8F8F;margin:0;max-width:600px}
.big{text-align:center;padding:90px 0 40px}.big h2{font-size:clamp(2.4rem,6vw,5rem);font-weight:500;line-height:1.05;letter-spacing:-.03em}
.foot{display:flex;justify-content:space-between;border-top:1px solid rgba(255,255,255,.08);padding:26px 0;margin-top:50px}
button[data-baseweb="tab"]{font-family:'JetBrains Mono';letter-spacing:.1em;text-transform:uppercase;font-size:.8rem}

.orbit{position:relative;width:540px;max-width:100%;height:540px;margin:auto}
.core{position:absolute;inset:0;margin:auto;width:130px;height:130px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;
 background:radial-gradient(circle at 30% 30%,#FFFFFF,#9A9A9A 60%,#1A1A1A);box-shadow:0 0 90px rgba(255,255,255,.5);font-size:2.6rem;animation:pulse 3s infinite}
.core small{font-family:'JetBrains Mono';font-size:.6rem;letter-spacing:.2em;color:#030303;font-weight:700}
.ring{position:absolute;inset:0;margin:auto;border-radius:50%;border:1px dashed rgba(255,255,255,.14);animation:rot var(--d) linear infinite}
@keyframes rot{to{transform:rotate(360deg)}}
@keyframes rotr{from{transform:rotate(calc(var(--t)*-1))}to{transform:rotate(calc(var(--t)*-1 - 360deg))}}
.ico{position:absolute;top:50%;left:50%;width:52px;height:52px;margin:-26px;transform:rotate(var(--t)) translateX(var(--r))}
.ico i{display:flex;width:52px;height:52px;align-items:center;justify-content:center;font-style:normal;font-size:1.5rem;border-radius:16px;cursor:default;
 background:rgba(10,10,10,.9);border:1px solid rgba(255,255,255,.14);backdrop-filter:blur(8px);animation:rotr var(--d) linear infinite;transition:.3s}
.ico i:hover{border-color:#E8E8E8;box-shadow:0 0 25px rgba(255,255,255,.6)}
.grp{padding:20px 22px;border-radius:18px;background:rgba(10,10,10,.8);border:1px solid rgba(255,255,255,.08);margin-bottom:14px;transition:.3s}
.grp:hover{border-color:rgba(255,255,255,.5);transform:translateX(6px)}
.fact{display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.08)}
.fact b{font-weight:500;color:#F2F2F2}
.jc{padding:26px;border-radius:20px;background:rgba(10,10,10,.8);border:1px solid rgba(255,255,255,.08);height:100%}
.jc h3{font-size:1.4rem;font-weight:500;margin:12px 0 8px}.jc p{color:#8F8F8F;font-size:.93rem;line-height:1.6}

.hero2{position:relative;height:min(88vh,800px);margin-top:10px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.hero2 .top{position:absolute;top:18px;left:0;right:0;text-align:center;z-index:5}
.nm{position:absolute;top:50%;margin:0;line-height:1;white-space:nowrap;font-size:clamp(3.6rem,12.2vw,12rem);font-weight:700;letter-spacing:-.045em;transform:translateY(-58%)}
.nm.a{left:0;z-index:1;color:#F2F2F2}
.nm.b{right:1%;z-index:3;font-weight:400;letter-spacing:-.02em;font-size:clamp(4rem,15vw,14.5rem)}
.ph{position:relative;z-index:2;width:clamp(240px,27vw,400px);aspect-ratio:3/4.2}
.ph:before{content:'';position:absolute;inset:-12% -30%;background:radial-gradient(closest-side,rgba(255,255,255,.18),rgba(255,255,255,.05) 55%,transparent);filter:blur(30px)}
.ph img,.ph .fb{position:relative;width:100%;height:100%;object-fit:cover;border-radius:30px;-webkit-mask-image:linear-gradient(#000 72%,transparent);mask-image:linear-gradient(#000 72%,transparent)}
.ph .fb{display:flex;align-items:center;justify-content:center;font-family:'Instrument Serif',serif;font-style:italic;font-size:9rem;color:#F2F2F2;background:linear-gradient(160deg,#E8E8E833,#9A9A9A33 60%,transparent);border:1px solid rgba(255,255,255,.12)}
.side{position:absolute;bottom:26px;z-index:5;line-height:2}.side.l{left:0}.side.r{right:0;text-align:right}
.sub{text-align:center;max-width:680px;margin:6px auto 0}.sub p{color:#9A9A9A;font-size:1.18rem;line-height:1.7}
@keyframes pl{to{transform:translate(-22vw,-58%)}}
@keyframes pr{to{transform:translate(22vw,-58%)}}
@keyframes pz{to{transform:translateY(-9%) scale(1.22)}}
@supports (animation-timeline:view()){
 .hero2 .nm.a{animation:pl linear both;animation-timeline:view();animation-range:exit 0% exit 100%}
 .hero2 .nm.b{animation:pr linear both;animation-timeline:view();animation-range:exit 0% exit 100%}
 .hero2 .ph{animation:pz linear both;animation-timeline:view();animation-range:exit 0% exit 100%}
}
@media(max-width:800px){.side{display:none}.nm{font-size:19vw}.nm.b{font-size:21vw}.ph{width:62vw}}

.stage{position:relative;height:calc(100vh - 20px);min-height:560px;display:flex;align-items:center;justify-content:center;perspective:1300px;overflow:clip}
.stage .top{position:absolute;top:84px;left:0;right:0;text-align:center;z-index:5}
.stage .sub{position:absolute;bottom:30px;left:50%;transform:translateX(-50%);width:min(540px,44vw);z-index:6;margin:0}
.stage .sub p{font-size:1rem;line-height:1.55;margin:0}
.stage .btn{margin:12px 6px 0}
@keyframes outL{0%{transform:translate(0,-58%) rotateY(0)}100%{transform:translate(-58vw,-58%) rotateY(42deg);opacity:0}}
@keyframes outR{0%{transform:translate(0,-58%) rotateY(0)}100%{transform:translate(58vw,-58%) rotateY(-42deg);opacity:0}}
@keyframes outP{0%{transform:translateZ(0) rotateX(0);opacity:1;filter:blur(0)}50%{opacity:1;filter:blur(0)}100%{transform:translateZ(560px) rotateX(16deg) translateY(-10%);opacity:0;filter:blur(18px)}}
@keyframes outT{0%{opacity:1}40%,100%{opacity:0;visibility:hidden}}
@keyframes rise{from{opacity:0;transform:translateY(70px) rotateX(12deg) scale(.95)}}
@supports (animation-timeline:scroll()){
 .hero3{height:150vh;margin-bottom:-50vh}
 .stage{position:sticky;top:0;height:100vh;z-index:1;pointer-events:none}
 .stage .sub{pointer-events:auto}
 .stage .nm.a{animation:outL linear both}
 .stage .nm.b{animation:outR linear both}
 .stage .ph{animation:outP linear both}
 .stage .top,.stage .side,.stage .sub{animation:outT linear both}
 .stage .nm.a,.stage .nm.b,.stage .ph,.stage .top,.stage .side,.stage .sub{animation-timeline:scroll(nearest block);animation-range:0px 46vh}
 .marq,.stat,.sec,.grp,.jc,.big,.wf{animation:rise linear both;animation-timeline:view();animation-range:entry 0% entry 55%}
 .card{animation:spin 5s linear infinite,rise linear both;animation-timeline:auto,view();animation-range:normal,entry 0% entry 55%}
}
@media(max-width:800px){.stage .sub{width:86vw}}

.core{font-family:'Instrument Serif',serif;font-style:italic;font-size:2.8rem!important;color:#030303;font-weight:400}
.core small{font-family:'JetBrains Mono';font-style:normal;font-size:.5rem!important;letter-spacing:.18em}
.ring{border:1px dashed rgba(255,255,255,.25)}
.ring:after{content:'';position:absolute;top:-4px;left:50%;width:8px;height:8px;margin-left:-4px;border-radius:50%;background:#E8E8E8;box-shadow:0 0 16px 3px #E8E8E8}
.ico i{background:linear-gradient(145deg,#fff,#d6dff3)!important;border:none!important;color:#0A0A0A;font-weight:700;font-size:.8rem!important;font-family:'JetBrains Mono';
 width:58px!important;height:58px!important;border-radius:18px!important;box-shadow:0 10px 26px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.5)}
.ico i:hover{box-shadow:0 0 30px 4px rgba(255,255,255,.75),0 0 0 1px #E8E8E8;transform:scale(1.18)}
.ico i img{width:32px;height:32px}
.ico{width:58px!important;height:58px!important;margin:-29px!important}
.wf{display:grid;grid-template-columns:70px 1.1fr 1.7fr 1fr;gap:30px;align-items:center;padding:34px 8px;border-top:1px solid rgba(255,255,255,.1);transition:.4s}
.wf:last-child{border-bottom:1px solid rgba(255,255,255,.1)}
.wf:hover{background:linear-gradient(90deg,rgba(255,255,255,.08),transparent);padding-left:22px}
.wf .no{color:#E8E8E8}.wf h3{font-size:clamp(1.8rem,3vw,2.6rem);font-weight:500;margin:0 0 6px;letter-spacing:-.02em}
.wf p{color:#8F8F8F;line-height:1.7;margin:0}.wf .tl2{color:#E8E8E8;line-height:1.8}
@media(max-width:800px){.wf{grid-template-columns:1fr;gap:10px}}

.feat{padding:44px;border-radius:26px;background:linear-gradient(160deg,#101010,#070707);border:1px solid rgba(255,255,255,.1);margin-bottom:26px}
.feat h3{font-size:clamp(1.8rem,3.4vw,3rem);font-weight:500;margin:14px 0;letter-spacing:-.02em}
.feat .lead{color:#9A9A9A;font-size:1.12rem;line-height:1.75;max-width:880px;margin:0 0 20px}
.sh{margin:38px 0 16px}
.pg{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.step,.mod{padding:24px;border-radius:18px;background:#0A0A0A;border:1px solid rgba(255,255,255,.08);transition:.3s}
.step:hover,.mod:hover{border-color:rgba(255,255,255,.4);transform:translateY(-5px)}
.step .no{color:#E8E8E8}.step h4,.mod h4{font-size:1.15rem;font-weight:500;margin:10px 0 8px}
.step p,.mod p{color:#8F8F8F;font-size:.9rem;line-height:1.6;margin:0}
.mods{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:900px){.pg{grid-template-columns:1fr 1fr}.mods{grid-template-columns:1fr}.feat{padding:26px}}
@supports (animation-timeline:scroll()){.feat,.step,.mod{animation:rise linear both;animation-timeline:view();animation-range:entry 0% entry 55%}}

:root{--pw:min(clamp(260px,30vw,470px),46vh)}
.stage{align-items:flex-start!important;padding-top:104px;height:calc(100vh - 70px)!important;min-height:600px}
.ph{width:var(--pw)}
.nm{top:calc(104px + var(--pw)*.7)!important}
.nm.b{right:1%;z-index:3;font-weight:700;letter-spacing:-.045em;font-size:clamp(3.6rem,12.2vw,12rem);background:linear-gradient(90deg,#FFFFFF,#8F8F8F);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stage .top{top:70px!important}.stage .sub{bottom:30px!important}
@keyframes outT{0%,50%{opacity:1}100%{opacity:0;visibility:hidden}}
.nav{position:fixed!important;top:14px;left:50%;transform:translateX(-50%);width:min(1100px,92vw);z-index:9999;margin:0!important;padding:10px 12px 10px 24px!important;
 background:rgba(20,20,20,.85)!important;border:1px solid rgba(255,255,255,.25)!important;box-shadow:0 12px 44px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,255,255,.12)}
.nav b{font-size:1.2rem}.nav a{color:#E8E8E8!important;font-size:.95rem!important;padding:9px 16px;border-radius:99px;margin:0 2px!important}
.nav a:hover{background:rgba(255,255,255,.14)}
.nav a.cta{background:#fff!important;color:#030303!important;font-weight:700;margin-left:8px!important;box-shadow:0 0 26px rgba(255,255,255,.35)}
.sec{border-top:1px solid rgba(255,255,255,.14);padding-top:38px}
.sec:after{content:attr(data-n);position:absolute;right:0;top:6px;font-family:'Instrument Serif',serif;font-style:italic;font-size:9rem;line-height:1;color:rgba(255,255,255,.05)}
.sh{display:flex;align-items:center;gap:14px;margin:38px 0 16px}.sh:after{content:'';flex:1;height:1px;background:rgba(255,255,255,.14)}
.panel{border-radius:32px;border:1px solid rgba(255,255,255,.16);background:linear-gradient(180deg,#0E0E0E,#060606);padding:30px 40px 36px;box-shadow:0 40px 100px rgba(0,0,0,.6)}
.pbar{display:flex;justify-content:space-between;align-items:center;padding-bottom:18px;border-bottom:1px solid rgba(255,255,255,.12);margin-bottom:26px}
.pbar.end{border-bottom:0;border-top:1px solid rgba(255,255,255,.12);margin:36px 0 0;padding:18px 0 0}
.panel .feat{background:none;border:0;padding:0;margin:0}.panel .step,.panel .mod{background:#121212}
.ab{color:#9A9A9A;line-height:1.85;font-size:1.1rem;margin:0 0 16px}
.why{display:grid;grid-template-columns:50px 1fr;gap:14px;padding:20px 0;border-top:1px solid rgba(255,255,255,.1)}
.why h4{margin:0 0 6px;font-size:1.2rem;font-weight:500}.why p{color:#8F8F8F;margin:0;line-height:1.6}.why .no{color:#E8E8E8}
.sg{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.sc{padding:20px;border-radius:18px;background:#0A0A0A;border:1px solid rgba(255,255,255,.1);transition:.3s}
.sc:hover{border-color:rgba(255,255,255,.5);transform:translateY(-4px)}
.sc .e{font-size:1.6rem}.sc h4{margin:8px 0 4px;font-size:1.05rem;font-weight:500}.sc p{color:#8F8F8F;font-size:.85rem;margin:0 0 10px}
@media(max-width:900px){.sg{grid-template-columns:1fr}.panel{padding:20px}}

.nm.b{right:auto!important;left:calc(50% + var(--pw)*.5 - 2.5vw)}
@keyframes navOut{0%,12%{opacity:1;transform:translateX(-50%) translateY(0)}100%{opacity:0;transform:translateX(-50%) translateY(-46px);visibility:hidden}}
@supports (animation-timeline:scroll()){.nav{animation:navOut linear both;animation-timeline:scroll(nearest block);animation-range:0px 30vh}}
.stApp{isolation:isolate}
.stApp:before,.stApp:after{content:'';position:fixed;inset:-25%;z-index:-1;pointer-events:none;filter:blur(70px)}
.stApp:before{background:radial-gradient(38% 34% at 22% 30%,rgba(255,255,255,.11),transparent 70%),radial-gradient(34% 30% at 78% 62%,rgba(200,200,200,.09),transparent 70%);animation:fog1 26s ease-in-out infinite alternate}
.stApp:after{background:radial-gradient(44% 38% at 72% 18%,rgba(255,255,255,.09),transparent 70%),radial-gradient(40% 34% at 28% 82%,rgba(170,170,170,.1),transparent 70%);animation:fog2 34s ease-in-out infinite alternate}
@keyframes fog1{to{transform:translate3d(9%,7%,0) scale(1.18) rotate(7deg)}}
@keyframes fog2{to{transform:translate3d(-10%,-6%,0) scale(1.22) rotate(-9deg)}}
@media(prefers-reduced-motion:reduce){.stApp:before,.stApp:after{animation:none}}

:root{--fs:clamp(3.6rem,12.2vw,12rem)}
.h2,.sec h2,.big h2{font-family:'Space Grotesk',sans-serif}
.h2{font-size:clamp(2.2rem,5vw,3.8rem);font-weight:500;line-height:1.05;margin:6px 0 24px;letter-spacing:-.025em}
.h2 .it,.sec h2 .it,.big h2 .it{font-family:inherit!important;font-style:normal!important;font-weight:inherit!important;font-size:1em!important}
.nav{position:absolute!important;top:16px;z-index:30;width:min(1100px,92%)}
.stage .nav{pointer-events:auto}
.nm.a{z-index:1}.ph{z-index:3!important}.nm.b{z-index:4!important}
.spider{position:absolute;z-index:2;width:100px;height:100px;left:-10%;pointer-events:none;
 top:calc(104px + var(--pw)*.7 - var(--fs)*.41 - 54px);animation:crawl 28s linear 1.2s infinite;
 filter:drop-shadow(0 6px 7px rgba(0,0,0,.85)) drop-shadow(0 0 9px rgba(255,255,255,.22))}
.spider .bob{animation:bob .5s ease-in-out infinite}
@keyframes crawl{0%{left:-10%}30%{left:30%}37%{left:34%}72%{left:80%}88%{left:110%}100%{left:110%}}
@keyframes bob{50%{transform:translateY(-2.5px)}}
@keyframes swL{0%,100%{transform:rotate(-13deg)}50%{transform:rotate(13deg)}}
@keyframes swR{0%,100%{transform:rotate(13deg)}50%{transform:rotate(-13deg)}}
.lgL{animation:swL .5s ease-in-out infinite}.lgR{animation:swR .5s ease-in-out infinite}
@supports (animation-timeline:scroll()){.stage .spider{animation:crawl 28s linear 1.2s infinite,outT linear both;animation-timeline:auto,scroll(nearest block);animation-range:normal,0px 46vh}}
@media(max-width:800px){.spider{display:none}}

.mcol{display:none}
@media(max-width:800px){
 html,body,.stApp,[data-testid=stMain]{overflow-x:hidden!important}
 .block-container{padding:.5rem 1rem 2rem!important;max-width:100vw!important}
 .nav{width:94%!important;padding:7px 7px 7px 14px!important;top:10px!important}
 .nav b{font-size:1rem}.nav .dot{display:none}.nav>div{display:flex;align-items:center}
 .nav a{padding:6px 8px!important;font-size:.76rem!important;margin:0 1px!important}.nav a.cta{margin-left:4px!important}
 .hero3{height:auto!important;margin-bottom:0!important}
 .stage{position:relative!important;height:auto!important;min-height:0!important;display:flex!important;flex-direction:column;align-items:center!important;padding:84px 0 10px!important;overflow:visible!important}
 .stage .nm,.stage .ph,.stage .top,.stage .sub{animation:none!important;opacity:1!important;visibility:visible!important}
 .stage .nm{position:static!important;transform:none!important;left:auto!important;right:auto!important;top:auto!important;font-size:17vw!important;text-align:center;z-index:5}
 .stage .nm.a{order:2;margin-top:-13vw}.stage .nm.b{order:3}
 .stage .ph{order:1;width:66vw!important;max-width:300px}
 .stage .top{position:static!important;order:0;margin-bottom:14px;font-size:.58rem!important;letter-spacing:.08em!important}
 .stage .mcol{display:block;order:4;text-align:center;font-size:.6rem;line-height:1.9;margin-top:14px}
 .stage .sub{position:static!important;transform:none!important;order:5;width:100%!important;margin-top:14px!important}
 .stage .sub p{font-size:.95rem}
 .side{display:none!important}
 .sec{margin-top:70px}.sec:after{font-size:5rem;top:20px}
 .fact{flex-direction:column;gap:3px}
 .panel{padding:18px 14px!important;border-radius:22px}
 .pbar{flex-direction:column;align-items:flex-start;gap:6px}
 .pg{grid-template-columns:1fr!important}.feat h3{font-size:1.6rem}
 .orbit{width:540px!important;max-width:none!important;position:relative;left:50%;margin:0 0 -205px -270px!important;transform:scale(.62);transform-origin:center top}
 .foot{flex-direction:column;gap:6px;text-align:center}
}
</style>
""", unsafe_allow_html=True)

nav = {"about": "About", "work": "Project", "skills": "Skills"}
nav_html = f"""<div class="nav"><b><span class="dot"></span>{D['first']}<span class="it">.</span></b><div>
{''.join(f'<a href="#{k}">{v}</a>' for k, v in nav.items())}<a class="cta" href="#contact">Let's talk</a></div></div>"""

uri = photo_uri()
img = f'<img src="{uri}" alt="{D["first"]} {D["last"]}">' if uri else f'<div class="fb">{D["first"][0]}</div>'
st.markdown(f"""<div class="hero3"><div class="stage">
{nav_html}
<div class="top mono"><span class="typed">{D['typed']}</span></div>
<div class="side l mono">{D['role']}<br>B.Tech · CSE (Data Science)<br>Technocrats Institute of Technology<br>Bhopal</div>
<div class="nm a">{D['first'].upper()}</div>
<div class="ph">{img}</div>
<div class="nm b">{D['last'].upper()}</div>
<div class="side r mono">Based in {D['location']}<br>Scroll to discover ↓</div>
<div class="mcol mono">{D['role']} · B.Tech CSE (Data Science)<br>Technocrats Institute of Technology, Bhopal</div>
<div class="sub"><p>{D['tagline']}</p>
<a class="btn p" href="#work">View my project</a><a class="btn s" href="#contact">Contact me</a></div>
</div></div>""", unsafe_allow_html=True)

tools = "".join(f"<span>{t}</span>" for t in D["tools"] * 2)
st.markdown(f'<div class="marq"><div>{tools}</div></div>', unsafe_allow_html=True)


a, b = D["about_big"]
st.markdown('<div id="about" class="sec" data-n="01" style="margin-bottom:0"><div class="mono">01 / About me</div></div>', unsafe_allow_html=True)
ab1, ab2 = st.columns([1.35, 1], gap="large")
with ab1:
    paras = "".join(f"<p class='ab'>{t}</p>" for t in D["about"])
    why = "".join(f'<div class="why"><div class="mono no">0{i}</div><div><h4>{t}</h4><p>{d}</p></div></div>' for i, (t, d) in enumerate(D["why"], 1))
    st.markdown(f'<h2 class="h2">{a} <span class="it">{b}</span></h2>' + paras + '<div class="mono sh" style="margin-top:34px">Why hire me</div>' + why, unsafe_allow_html=True)
with ab2:
    rows = "".join(f'<div class="fact"><span class="mono">{a_}</span><b>{b_}</b></div>' for a_, b_ in D["facts"])
    st.markdown(f'<div class="grp" style="padding:10px 26px;margin-top:10px">{rows}</div><a class="btn p" href="{D["github"]}" target="_blank">GitHub</a><a class="btn s" href="{D["linkedin"]}" target="_blank">LinkedIn</a>', unsafe_allow_html=True)

P = D["project"]
steps = "".join(f'<div class="step"><div class="mono no">0{i}</div><h4>{t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate(P["steps"], 1))
mods = "".join(f'<div class="mod"><h4>{t}</h4><p>{d}</p></div>' for t, d in P["modules"])
models = "".join(f'<span class="chip">{m}</span>' for m in P["models"])
stack = "".join(f'<span class="chip">{m}</span>' for m in P["stack"])
btns = (f'<a class="btn p" href="{P["github"]}" target="_blank">View on GitHub</a>' if P["github"] else "") + (f'<a class="btn s" href="{P["demo"]}" target="_blank">Live demo</a>' if P["demo"] else "")
st.markdown(f'''<div id="work" class="sec" data-n="02"><div class="mono">02 / Featured project</div><h2>End to end <span class="it">project.</span></h2></div><br>
<div class="panel"><div class="pbar"><span class="mono">● Project starts</span><span class="mono">{P["tag"]}</span></div>
<div class="feat"><h3>{P["name"]}</h3><p class="lead">{P["summary"]}</p><div>{btns}</div></div>
<div class="mono sh">The pipeline</div><div class="pg">{steps}</div>
<div class="mono sh">What the app does</div><div class="mods">{mods}</div>
<div class="mono sh">Models compared</div><div>{models}</div>
<div class="mono sh">Skills used in this project</div><div>{stack}</div>
<div class="pbar end"><span class="mono">● Project ends</span><a class="mono" href="#skills" style="color:#F2F2F2;text-decoration:none">Next: skills ↓</a></div></div>''', unsafe_allow_html=True)

st.markdown('<div id="skills" class="sec" data-n="03"><div class="mono">03 / Technical skills</div><h2>Technical <span class="it">skills.</span></h2><p class="ab" style="margin-top:14px">Hover over the orbiting icons to explore the stack.</p></div><br>', unsafe_allow_html=True)
sk1, sk2 = st.columns([1.1, 1], gap="large", vertical_alignment="center")
R = {1: (100, 26), 2: (170, 38), 3: (240, 52)}
with sk1:
    html = '<div class="orbit"><div class="core">DS<small>DATA SCIENCE</small></div>'
    for ring, (r, dur) in R.items():
        items = [o for o in D["orbit"] if o[0] == ring]
        html += f'<div class="ring" style="width:{2*r}px;height:{2*r}px;--d:{dur}s">'
        for i, (_, kind, val, lab) in enumerate(items):
            u = icon_uri(val) if kind == "icon" else None
            inner = f'<img src="{u}" alt="{lab}">' if u else (val if kind == "text" else lab[:3])
            html += f'<div class="ico" style="--t:{i*360//len(items)}deg;--r:{r}px;--d:{dur}s"><i title="{lab}">{inner}</i></div>'
        html += '</div>'
    st.markdown(html + '</div>', unsafe_allow_html=True)
with sk2:
    cards = "".join(f'<div class="sc"><h4>{g}</h4><p>{d}</p>' + "".join(f'<span class="chip">{t}</span>' for t in ts) + '</div>' for g, (e, d, ts) in D["groups"].items())
    st.markdown(f'<div class="sg">{cards}</div>', unsafe_allow_html=True)

st.markdown(f"""<div id="contact" class="big"><div class="mono">04 / Contact</div>
<h2>Something great<br>starts with <span class="it">a hello.</span></h2>
<a class="btn p" href="mailto:{D['email']}">Let's connect</a><a class="btn s" href="{D['linkedin']}" target="_blank">LinkedIn</a><a class="btn s" href="{D['github']}" target="_blank">GitHub</a></div>""", unsafe_allow_html=True)
if os.path.exists("resume.pdf"):
    with open("resume.pdf", "rb") as f:
        st.download_button("⬇ Download Resume", f, "Resume.pdf", use_container_width=True)
st.markdown(f'<div class="foot mono"><span>{D["first"]} {D["last"]}.</span><span>Designed &amp; built by me, in Python</span><span>{D["location"]}</span></div>', unsafe_allow_html=True)

try:  # optional extra: sets the tab icon from the page itself (page_icon above already does it)
    import streamlit.components.v1 as components
    components.html(f"""<script>
const d = window.parent.document;
d.querySelectorAll("link[rel*='icon']").forEach(l => l.remove());
const l = d.createElement("link"); l.rel = "icon"; l.type = "image/png"; l.href = "data:image/png;base64,{FAVICON}";
d.head.appendChild(l);
</script>""", height=0)
except Exception:
    pass
