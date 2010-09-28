" File: scratch.vim
" Author: Yegappan Lakshmanan (yegappan AT yahoo DOT com)
" Version: 1.0
" Last Modified: June 3, 2003
if exists('loaded_scratch') || &cp
    finish
endif
let loaded_scratch=1
let ScratchBufferName = $HOME."/.vim/Buffer-".@%.".tmp"
function! s:ScratchBufferOpen(new_win)
    exe "6sp " . g:ScratchBufferName
endfunction
function! s:ScratchMarkBuffer()
    setlocal buftype=nofile
    setlocal bufhidden=hide
    setlocal noswapfile
    setlocal buflisted
endfunction
autocmd BufNewFile __Scratch__ call s:ScratchMarkBuffer()
command! -nargs=0 Scratch call s:ScratchBufferOpen(0)
command! -nargs=0 Sscratch call s:ScratchBufferOpen(1)
