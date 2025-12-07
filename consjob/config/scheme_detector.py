"""
Scheme interpreter detection module.

Detects common Scheme implementations installed on the system.
"""

import shutil
import subprocess
from dataclasses import dataclass
from typing import Optional


@dataclass
class SchemeInterpreter:
    """Represents a detected Scheme interpreter."""
    name: str
    path: str
    version: Optional[str] = None
    
    def display_name(self) -> str:
        """Return a user-friendly display name."""
        if self.version:
            return f"{self.name} ({self.version})"
        return self.name


# Common Scheme interpreters to search for
# Format: (command_name, display_name, version_args, version_parser)
KNOWN_INTERPRETERS = [
    ("mit-scheme", "MIT/GNU Scheme", ["--version"], lambda out: out.split('\n')[0].strip() if out else None),
    ("scheme", "Chez Scheme", ["--version"], lambda out: out.strip() if out else None),
    ("chez", "Chez Scheme", ["--version"], lambda out: out.strip() if out else None),
    ("guile", "GNU Guile", ["--version"], lambda out: out.split('\n')[0].strip() if out else None),
    ("chibi-scheme", "Chibi-Scheme", None, None),  # No simple version flag
    ("chicken", "CHICKEN Scheme", ["-version"], lambda out: out.strip() if out else None),
    ("csi", "CHICKEN Scheme (Interpreter)", ["-version"], lambda out: out.strip() if out else None),
    ("gsi", "Gambit Scheme", ["-v"], lambda out: out.strip() if out else None),
    ("gambit", "Gambit Scheme", ["-v"], lambda out: out.strip() if out else None),
    ("tinyscheme", "TinyScheme", None, None),  # No version flag
    ("ikarus", "Ikarus Scheme", ["--version"], lambda out: out.strip() if out else None),
    ("racket", "Racket", ["--version"], lambda out: out.strip() if out else None),
    ("kawa", "Kawa Scheme", ["--version"], lambda out: out.strip() if out else None),
]


def get_interpreter_version(path: str, version_args: list, version_parser) -> Optional[str]:
    """Try to get the version string for an interpreter."""
    if not version_args or not version_parser:
        return None
    
    try:
        result = subprocess.run(
            [path] + version_args,
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout or result.stderr
        if output:
            return version_parser(output)
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, OSError):
        pass
    
    return None


def detect_scheme_interpreters() -> list[SchemeInterpreter]:
    """
    Detect all installed Scheme interpreters on the system.
    
    Returns:
        A list of SchemeInterpreter objects for each detected interpreter.
    """
    detected = []
    seen_paths = set()  # Avoid duplicates (e.g., 'scheme' and 'chez' pointing to same binary)
    
    for cmd, display_name, version_args, version_parser in KNOWN_INTERPRETERS:
        path = shutil.which(cmd)
        if path and path not in seen_paths:
            seen_paths.add(path)
            version = get_interpreter_version(path, version_args, version_parser)
            detected.append(SchemeInterpreter(
                name=display_name,
                path=path,
                version=version
            ))
    
    return detected


def get_default_interpreter() -> Optional[SchemeInterpreter]:
    """
    Get the default/preferred Scheme interpreter.
    
    Preference order: MIT Scheme > Guile > Chez > Chibi > CHICKEN > others
    
    Returns:
        The preferred SchemeInterpreter, or None if none are installed.
    """
    interpreters = detect_scheme_interpreters()
    
    if not interpreters:
        return None
    
    # Return first match (list is already in preference order)
    return interpreters[0]


def is_valid_interpreter(path: str) -> bool:
    """
    Check if a given path is a valid, executable Scheme interpreter.
    
    Args:
        path: Path to the interpreter executable.
        
    Returns:
        True if the path exists and is executable.
    """
    if not path:
        return False
    
    # Use shutil.which to verify it's executable
    # If it's an absolute path, check directly
    import os
    if os.path.isabs(path):
        return os.path.isfile(path) and os.access(path, os.X_OK)
    
    return shutil.which(path) is not None
