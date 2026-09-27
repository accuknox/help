import annotate as a
SHOTS = a.OUT
from playwright.sync_api import sync_playwright
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
MENUS=[("N1","Secure AI",[("N1","ADD","AI SPM – Security Posture Management",0),("N2","FIX","AI Identity Security",0)]),
       ("N3","Secure Code",[("N3","FIX","AI-Accelerated SAST Scanning",0)]),
       ("N4","Coming Soon",[("N4","MOVE","Data Security (DSPM)",0)])]
with sync_playwright() as p:
    try: br=p.chromium.launch(channel="chrome", args=["--disable-blink-features=AutomationControlled"])
    except Exception: br=p.chromium.launch(args=["--disable-blink-features=AutomationControlled"])
    ctx=br.new_context(viewport={"width":1440,"height":900}, user_agent=UA)
    ctx.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
    pg=ctx.new_page()
    # extra targets on content pages
    for path, anns in [] and [("/platform/ai-security",[("A6","REPLACE","AI Security for AI/LLM Workload Security FAQs",1)]),
                       ("/solutions/sast",[("S2","UPDATE","SAST Solution",1)])]:
        a.prep(pg, a.B+path); pg.wait_for_timeout(3000)
        for code, action, text, up in anns:
            box=pg.evaluate(a.JS_FIND,[text,up]); print(code, bool(box))
            if box:
                pg.evaluate(a.JS_DRAW,[box,code,action,a.COLORS[action]])
                pg.screenshot(path=str(SHOTS / f"{code}.png"), full_page=True, clip={"x":0,"y":max(0,box["y"]-110),"width":1440,"height":min(box["h"]+190,1300)})
    for fname, item, anns in MENUS:
        pg.goto(a.B+"/", wait_until="domcontentloaded"); pg.wait_for_timeout(3500)
        try: pg.get_by_role("button", name="Reject All").first.click(timeout=2500)
        except Exception: pass
        pg.get_by_text("Platform", exact=True).first.hover(); pg.wait_for_timeout(1200)
        F0=a.JS_FIND.replace("for (let i = 0; i < 6","for (let i = 0; i < 0")
        b=pg.evaluate(F0,[item,0]); print(item,b)
        pg.mouse.move(b["x"]+20, b["y"]+b["h"]/2, steps=8); pg.wait_for_timeout(1500)
        for code, action, text, up in anns:
            box=pg.evaluate(a.JS_FIND.replace("for (let i = 0; i < 6","for (let i = 0; i < 0"),[text,up]); print(code, box)
            if box: pg.evaluate(a.JS_DRAW,[box,code,action,a.COLORS[action]])
        pg.screenshot(path=str(SHOTS / f"{fname}-menu.png"), clip={"x":0,"y":0,"width":1440,"height":820})
    br.close()
