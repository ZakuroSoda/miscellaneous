## Pandoc (Minimum) Install Instructions (Particularly .md to .pdf)

1. https://pandoc.org/installing.html
2. Once done, do the usual PATH stuff
3. Check that `pandoc -h` works.
4. https://tug.org/texlive/windows.html (install-tl-windows.exe) -> You only need to install the basic package to save space.
5. Now run ` pandoc .\README.md -o README.pdf` and see what files it says are not found.  
   Use `tlmgr install [filename without the .sty]`
6. In my case, I needed to run  
   `tlmgr install xcolor` and  
   `tlmgr install etoolbox`