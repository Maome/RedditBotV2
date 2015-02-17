import time
import praw

r = praw.Reddit('pretense')
r.login('timewaitsforsome', '*')

dont_repost = 'empty'     

ignore_list = ['FreeBits','lounge']

delay = int(time.time())

while True:
    try:
        while(time.time() < delay):
            time.sleep(1)
        comms = praw.helpers.comment_stream(r, 'all', limit=None)
        for c in comms:
            if c.is_root:
                if len(c.body) < 50:
                    sub = c.submission
                    if sub.num_comments > 100:
                        if sub.url != dont_repost:
                            b = False
                            for item in ignore_list:
                                if item.lower() in sub.url.lower():
                                    print('Ignoring %s' % item)
                                    b = True
                                    break
                            if b:
                                continue
                            try:
                                sub.add_comment(c.body.lower().strip('.'))
                                dont_repost = sub.url
                                delay = time.time() + 30  
                                print c.permalink
                            except Exception as e:
                                delay = time.time() + 60 
                                print 'Extended delay'
                            break
    except Exception as e:
        print e
