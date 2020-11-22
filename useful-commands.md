## Куски кода, вставляемые в преамбулу

Отключает переносы, если они вам не нравятся, или нужно растянуть объем :)

```latex
\tolerance=1
\emergencystretch=\maxdimen
\hyphenpenalty=10000
\hbadness=10000
```

Подключает математические пакеты:

```latex
\usepackage{amsmath,amsthm,amssymb,breqn}
```

Указание пути к картинкам

```latex
\graphicspath{{images/}}
```

Указание пути к файлам, подключаемых через команду `\input`

```latex
\makeatletter\def\input@path{{inc/}}\makeatother
```

Включает возможность вставки исходников.
Нужен Python и Pygments. Подробнее [здесь](https://ru.overleaf.com/learn/latex/Code_Highlighting_with_minted).
Также добавьте опцию -shell-escape в BUILD в Makefile.

```latex
\usepackage[outputdir=build]{minted}
\usemintedstyle{bw}
% исправляет баг с redbox-ами
\makeatletter
\AtBeginEnvironment{minted}{\dontdofcolorbox}
\def\dontdofcolorbox{\renewcommand\fcolorbox[4][]{##4}}
\makeatother
```

Вставка списка источников из файла:

```latex
\addbibresource{refs.bib}
```

Используйте эту команду для генерации отчета только из указанных файлов.
Используется для ускорения сборки проекта:

```latex
\includeonly{1-Intro}
```

## Куски кода для основной части текста.

Создание таблицы (о да, это проблематичнее всего).

```latex
\noindent
\begin{tabularx}{\textwidth} {
    |>{\small\hsize=0.35\hsize\raggedright\arraybackslash}X
    |>{\small\hsize=0.65\hsize\raggedright\arraybackslash}X|}
\caption{НАЗВАНИЕ ТАБЛИЦЫ}\label{tab:mytab}\\
\hline
\textbf{Первый столбец} & \textbf{Второй столбец подлиннее}\\
\endfirsthead
\caption*{Продолжение таблицы \ref{tab:mytab}}\\
% \hline
% \textbf{Первый столбец} & \textbf{Второй столбец подлиннее}\\
\endhead
\hline
Оригинальное предложение & Показанный на рисунке
гидродинамический удар, безусловно, подрывает смысл жизни.\\
\hline
\multicolumn{2}{|>{\small\raggedright\arraybackslash}X|}%
{Сплошной столбец, почему бы и нет?}\\
\hline
\end{tabularx}
```

Вставка куска исходника:

```latex
\begin{codewrap}[0.5]
\begin{minted}[fontsize=\footnotesize]{python}
from nltk import sent_tokenize
from rtm.rutermextract import TermExtractor
import re
from latex import escape
\end{minted}
\caption{Импорт пакетов}\label{fig:import-code}
\end{codewrap}
```

Вставка исходника из файла:

```latex
\inputminted[fontsize=\footnotesize]{python}{inc/source.py}
```
