from PIL import Image
import ascii_magic
import re, os, time, tempfile

class terminalArt():
    fname = ""
    fn = ""
    coloring = ""
    RESET = '\033[0m'

    def clear(self):
        os.system("clear||cls")
    
    def __init__(self, fname):
        self.fname = fname

    def get_color_escape(self, r, g, b, background=False):
        self.coloring = '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

    
    def turnHtmlToTerminal(self):
        file = open(self.fn)
        text = file.readlines()
        pre = re.findall(r">(.*)</pre>", "".join(text))[0]
        spans = re.findall(r'<span style="color: #(\w+)">(.)</span>', pre)
        s = pre.split("<br />")[0]
        tor = 0
        for span in spans:
            tor += 1
            self.get_color_escape(int(span[0][:2], 16), int(span[0][2:4], 16), int(span[0][4:6], 16))
            print(self.coloring
            + span[1]
            + self.RESET, end="")
            if((len(s.split("</span>"))-1) == tor):
                print()
                tor = 0

    def main(self):
        if os.name == 'nt':
            from ctypes import windll
            k = windll.kernel32
            k.SetConsoleMode(k.GetStdHandle(-11), 7)

        self.clear()
        im = Image.open(self.fname)
        for tor in range(im.n_frames):
            filename = tempfile.gettempdir() + "/frame" + str(tor) + ".png"
            self.fn = tempfile.gettempdir() + "/frame" + str(tor) + ".html"
            im.seek(tor)
            im.save(filename)
            my_art = ascii_magic.from_image_file(
                filename,
                columns=50,
                width_ratio=2,
                mode=ascii_magic.Modes.HTML
            )
            self.clear()
            ascii_magic.to_html_file(self.fn, my_art)
            self.turnHtmlToTerminal()
            # time.sleep(0.05)
        
if __name__ == "__main__":
    tA = terminalArt("tor.gif")
    tA.main()