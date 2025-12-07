
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression

class SchemeHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for Scheme code."""
    
    def __init__(self, document):
        super().__init__(document)
        self.highlighting_rules = []

        # Colors (Hardcoded for now, should use Theme)
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#cba6f7"))
        keyword_format.setFontWeight(QFont.Weight.Bold)
        
        # Scheme keywords and special forms
        keywords = [
            # Core forms
            "define", "lambda", "let", "let\\*", "letrec", "letrec\\*",
            "set!", "if", "cond", "case", "when", "unless", "else",
            "begin", "do", "and", "or", "not",
            # Quoting
            "quote", "quasiquote", "unquote", "unquote-splicing",
            # Macros
            "define-syntax", "let-syntax", "letrec-syntax", "syntax-rules", "syntax-case",
            # Modules (R6RS/R7RS)
            "import", "export", "library", "include", "include-ci",
            "define-library", "cond-expand",
            # Delayed evaluation
            "delay", "force", "lazy",
            # Parameters
            "parameterize", "make-parameter",
        ]
        for word in keywords:
            pattern = QRegularExpression(f"\\({word}\\b|\\b{word}\\b")
            self.highlighting_rules.append((pattern, keyword_format))

        # Standard procedures
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#89b4fa"))
        functions = [
            # List operations
            "car", "cdr", "cons", "list", "append", "reverse", "length",
            "null\\?", "pair\\?", "list\\?", "symbol\\?", "number\\?", "string\\?", "boolean\\?",
            "procedure\\?", "vector\\?", "char\\?", "port\\?", "eof-object\\?",
            "cadr", "caddr", "cadddr", "cddr", "caar", "cdar",
            "list-ref", "list-tail", "list-set!", "list-copy",
            "assoc", "assq", "assv", "member", "memq", "memv",
            # Numeric operations
            "abs", "max", "min", "modulo", "quotient", "remainder",
            "floor", "ceiling", "truncate", "round",
            "sqrt", "expt", "log", "exp", "sin", "cos", "tan",
            "asin", "acos", "atan", "gcd", "lcm",
            "numerator", "denominator", "rationalize",
            # Numeric predicates
            "zero\\?", "positive\\?", "negative\\?", "odd\\?", "even\\?",
            "exact\\?", "inexact\\?", "nan\\?", "infinite\\?", "finite\\?",
            "integer\\?", "rational\\?", "real\\?", "complex\\?",
            # Comparison
            "eq\\?", "eqv\\?", "equal\\?",
            # String operations
            "string-append", "string-length", "substring", "string-ref",
            "string=\\?", "string<\\?", "string>\\?", "string<=\\?", "string>=\\?",
            "string->list", "list->string", "string->number", "number->string",
            "string-copy", "string-fill!", "string-set!",
            "string-upcase", "string-downcase",
            # Character operations  
            "char->integer", "integer->char", "char=\\?", "char<\\?",
            "char-alphabetic\\?", "char-numeric\\?", "char-whitespace\\?",
            # I/O
            "display", "newline", "read", "write", "read-line", "read-char", "write-char",
            "open-input-file", "open-output-file", "close-port", "close-input-port", "close-output-port",
            "current-input-port", "current-output-port", "current-error-port",
            "with-input-from-file", "with-output-to-file",
            "call-with-input-file", "call-with-output-file",
            "eof-object", "peek-char",
            # Vector operations
            "vector", "make-vector", "vector-length", "vector-ref", "vector-set!",
            "vector->list", "list->vector", "vector-fill!", "vector-copy",
            # Higher-order functions
            "map", "for-each", "filter", "fold", "fold-right", "reduce",
            "apply", "call/cc", "call-with-current-continuation",
            "call-with-values", "values", "dynamic-wind",
            # Control
            "error", "raise", "raise-continuable", "with-exception-handler",
            "guard",
            # Misc
            "load", "eval", "interaction-environment",
            "void", "identity",
        ]
        for word in functions:
            pattern = QRegularExpression(f"\\b{word}\\b")
            self.highlighting_rules.append((pattern, function_format))
        
        # Operators / Special symbols
        op_format = QTextCharFormat()
        op_format.setForeground(QColor("#89b4fa")) 
        ops = [r"\+", r"\-", r"\*", "/", "<", ">", "<=", ">=", "="]
        for op in ops:
             pattern = QRegularExpression(f"[{op}]")
             self.highlighting_rules.append((pattern, op_format))

        # Boolean literals
        bool_format = QTextCharFormat()
        bool_format.setForeground(QColor("#fab387"))
        bool_format.setFontWeight(QFont.Weight.Bold)
        self.highlighting_rules.append((QRegularExpression(r"#t\b|#f\b|#true\b|#false\b"), bool_format))

        # Strings
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#a6e3a1"))
        self.highlighting_rules.append((QRegularExpression(r'"[^"\\]*(\\.[^"\\]*)*"'), string_format))

        # Numbers (including Scheme-specific formats)
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#fab387"))
        # Integers, floats, rationals, and Scheme prefixes like #x, #o, #b, #e, #i
        self.highlighting_rules.append((QRegularExpression(r"\b-?[0-9]+(/[0-9]+)?(\.[0-9]+)?([eE][+-]?[0-9]+)?\b"), number_format))
        self.highlighting_rules.append((QRegularExpression(r"#[xXoObBdDeEiI][0-9a-fA-F]+"), number_format))
        
        # Characters (Scheme character literals)
        char_format = QTextCharFormat()
        char_format.setForeground(QColor("#f9e2af"))
        self.highlighting_rules.append((QRegularExpression(r"#\\(\w+|.)"), char_format))
        
        # Comments (line comments with ;)
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6c7086"))
        self.highlighting_rules.append((QRegularExpression(r";.*"), comment_format))
        
        # Datum comment (#;) - highlights the #; part
        datum_comment_format = QTextCharFormat()
        datum_comment_format.setForeground(QColor("#6c7086"))
        self.highlighting_rules.append((QRegularExpression(r"#;"), datum_comment_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)


# Keep LispHighlighter as an alias for backwards compatibility
LispHighlighter = SchemeHighlighter

