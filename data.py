

set_win = {
    "WIDTH": 800,
    "HEIGHT": 600

    }

set_ball = {
    "RADIUS": 20,
    "SPEED": 5,
}
set_board = {
    "WIDTH": 20,
    "HEIGHT": 100
}

start_game = {
    "LEFT_PLAYER": (20, set_win["HEIGHT"]//2 - set_board["HEIGHT"]//2),
    "RIGHT_PLAYER": (set_win["WIDTH"]- 40, set_win["HEIGHT"]//2 - set_board["HEIGHT"]//2),
    "BALL": {
        "START": (set_win["WIDTH"] // 2, set_win["HEIGHT"] // 2),
        "LEFT_PLAYER": (set_win["WIDTH"] // 2, set_win["HEIGHT"] // 2, -set_ball["SPEED"]),
        "RIGHT_PLAYER": (set_win["WIDTH"] // 2, set_win["HEIGHT"] // 2, set_ball["SPEED"])
    }
}








