from streamlit.components.v1 import html

def circular_score(score, title, label):

    card = f"""
    <html>
    <head>
    <style>
        body {{
            margin:0;
            background:#1E1E1E;
            font-family:Arial;
        }}

        .score-card {{
            background:#1E1E1E;
            border-radius:18px;
            padding:20px;
            text-align:center;
        }}

        .circle {{
            width:140px;
            height:140px;
            margin:auto;
            border-radius:50%;
            background:conic-gradient(#00c853 {score}%, #333 {score}% 100%);
            display:flex;
            justify-content:center;
            align-items:center;
        }}

        .inner {{
            width:105px;
            height:105px;
            background:#111;
            border-radius:50%;
            display:flex;
            justify-content:center;
            align-items:center;
            color:white;
            font-size:28px;
            font-weight:bold;
        }}

        .title {{
            color:white;
            font-size:20px;
            margin-bottom:15px;
            font-weight:bold;
        }}

        .label {{
            color:#00d084;
            margin-top:15px;
            font-size:18px;
        }}
    </style>
    </head>

    <body>

    <div class="score-card">

        <div class="title">{title}</div>

        <div class="circle">
            <div class="inner">
                {score:.1f}%
            </div>
        </div>

        <div class="label">{label}</div>

    </div>

    </body>
    </html>
    """

    html(card, height=260)