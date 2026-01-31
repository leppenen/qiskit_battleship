import numpy as np


def generate_positions(n: int, max_num: int = 63, bits: int = 6) -> list[str]:
    """Generate n unique random positions as binary strings.
    """
    
    # Use numpy to generate unique random positions
    positions_int = np.random.choice(max_num + 1, size=n, replace=False)
    
    # Convert to binary strings with proper bit width
    format_string = f"{{0:0{bits}b}}"
    positions = [format_string.format(pos) for pos in positions_int]
    
    return positions


def bitstring_to_coords(bitstring: str, board_size: int = 8) -> tuple[int, int]:
    """Convert binary string to 2D board coordinates.
    
    Args:
        bitstring: Binary string (e.g., '101011')
        board_size: Size of the square board (default 8 for 8x8)
    
    Returns:
        Tuple of (row, col) coordinates
    
    Example:
        >>> bitstring_to_coords('101011', board_size=8)
        (5, 3)
    """
    value = int(bitstring, 2)
    row = value // board_size
    col = value % board_size
    return (row, col)


def coords_to_bitstring(row: int, col: int, board_size: int = 8, bits: int = 6) -> str:
    """Convert 2D board coordinates to binary string.
    
    Args:
        row: Row index (0-based)
        col: Column index (0-based)
        board_size: Size of the square board (default 8 for 8x8)
        bits: Number of bits in output string
    
    Returns:
        Binary string representation
    
    Example:
        >>> coords_to_bitstring(5, 3, board_size=8)
        '101011'
    """
    value = row * board_size + col
    format_string = f"{{0:0{bits}b}}"
    return format_string.format(value)


def create_board_array(positions: list[str], board_size: int = 8) -> np.ndarray:
    """Create a 2D numpy array representing the battleship board.
    
    Args:
        positions: List of binary string positions
        board_size: Size of the square board
    
    Returns:
        2D numpy array with 1s at ship positions, 0s elsewhere
    
    Example:
        >>> positions = ['000000', '000111', '111111']
        >>> board = create_board_array(positions)
        >>> board.shape
        (8, 8)
    """
    board = np.zeros((board_size, board_size), dtype=int)
    
    for pos in positions:
        row, col = bitstring_to_coords(pos, board_size)
        if 0 <= row < board_size and 0 <= col < board_size:
            board[row, col] = 1
    
    return board


def get_classical_search_cost(n_positions: int, total_positions: int) -> float:
    """Calculate expected number of checks for classical random search.
    
    Args:
        n_positions: Number of ship positions to find
        total_positions: Total number of positions on the board
    
    Returns:
        Expected number of checks
    
    Note:
        For finding k items in N total positions, expected checks ≈ N(k+1)/(k+1) ≈ N/2
        when k << N
    """
    if n_positions >= total_positions:
        return float(total_positions)
    
    # Expected number of checks to find all k items
    expected_checks = total_positions * (np.log(total_positions) - np.log(total_positions - n_positions))
    
    return expected_checks