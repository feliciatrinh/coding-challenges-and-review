# Regex

[Documentation](https://docs.python.org/3/library/re.html)

| Character  | Function  | Example  |
|---|---|---|
| .  | Matches any character except a newline  |   |
| ^  | Matches start of the string  |   |
| $  | Matches end of the string  | `foo$` matches `foo` but not `foobar`  |
| *  | Match 0 or more repetitions of preceding RE  |   |
| +  | Match 1 or more repetitions of preceding RE  |   |
| ?  | Match 0 or 1 reps of preceding RE  | `ab?` matches either `a` or `ab`  |
| *?, +?, ??  | Adding `?` after the qualifier makes it non-greedy. Will match as few characters as possible  | `<.*>` matches entire string `<a> b <c>` but `<.*?>` matches only `<a>`  |
| {m}  | Match exactly m copies of preceding RE  |   |
| {m,n}  | Matches from m to n reps of preceding RE  | `a{3,5}` matches 3 to 5 `a` characters  |
| {m,n}?  | Matches m to n reps of preceding RE, but as few reps as possible  | `a{3,5}` on `aaaaa` will match only 3 characters  |
| \  | Escape special characters  |   |
| []  | Indicates a set of characters  | `[0-5][0-9]` are two-digit numbers from `00` to `59`  |
| &#124;  | <code>A&#124;B</code> where `A` and `B` are arbitrary REs created an RE that matches either A or B  |   |
| (...)  | Matches whatever RE is inside the parentheses  |   |
| \d  | Matches any decimal digit  | equivalent to `[0-9]`  |
| \D  | Matches any character not a decimal digit  | equivalent to `[^0-9]`  |
| \s  | Matches any whitespace characters  | equivalent to `[ \t\n\r\f\v]`  |
| \S  | Opposite of `\s`  |   |
| \w  | Matches alphanumeric characters  | equivalent to `[a-zA-Z0-9_]`  |
| \W  | Opposite of `\w`  |   |

* Special characters lose their special meaning inside sets.
    * Example: `[(+*)]` will match any of literal characters `(`, `+`, `*`, or `)`.
* Complement the set to match characters not within a range.
    * Example: `[^5]` matches any character except `5`
    
### Common Python module functions

`import re`

`re.search(pattern, string)`

`re.match(pattern, string)`

`re.fullmatch(pattern, string)`

`re.findall(pattern, string)`

`re.sub(pattern, repl, string)`