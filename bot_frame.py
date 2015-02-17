import time
import praw

class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.delay_until = int(time.time())
        self.reddit = None

    ### Implement these 3 in derived class
    def accept_comment(self, comment):
        return True

    def reject_comment(self, comment):
        return False

    def do_action(self, comment):
        pass

    def _wait_out_delay(self):
        wait_left = self.delay_until - time.time()
        if wait_left > 0:
            time.sleep(wait_left)

    def _get_comment_stream(self):
        cs = praw.helpers.comment_stream(self.reddit, 'all', limit=50)
        return cs

    def run(self):
        self.reddit = praw.Reddit('pretense2')
        self.reddit.login(self.username, self.password)

        while True:
            try:
                self._wait_out_delay()
                comments = self._get_comment_stream()
                for comment in comments:
                    if not self.accept_comment(comment):
                        continue
                    if self.reject_comment(comment):
                        continue
                    try:
                        #print('Trying to do action')
                        self.do_action(comment)
                    except Exception as e:
                        print(e)
                        self.delay_until = time.time() + 30
                    break
            except Exception as e:
                print(e)





