import string
from bot_frame import Bot
from sentence_modifier import modify_sentence
import passwd

class CommentModifyBot(Bot):
    dont_repost_url = ''

    def reject_comment(self, comment):
        if not comment.is_root:
            #print('Not root')
            return True
        submission = comment.submission
        if len(comment.body) < 15:
            #print('short')
            return True
        if len(comment.body) > 60:
            #print('long')
            return True
        if submission.num_comments < 50:
            #print('Not busy')
            return True
        if self.dont_repost_url == submission.url:
            #print('repost')
            return True
        #print('accept')
        return False

    def do_action(self, comment):
        #print('Doing action')
        submission = comment.submission
        self.dont_repost = submission.url
        sentence = comment.body.lower()
        sentence = sentence.translate(string.maketrans("",""),
                string.punctuation)
        modified = modify_sentence(sentence)
        if modified.strip() == sentence.strip():
            print("They were the same.. :(")
            return
        print("  %s" % submission.url)
        print("  Original:%s" % sentence)
        print("  Modified:%s" % modified)
        submission.add_comment(modified)
        #print('Action did')

def main():
    bot = CommentModifyBot(passwd.username, passwd.password)
    bot.run()

main()
