async def check_user(id):
    if CHANNEL is None:     # incase no join check is needed
        return True
    ok = True
    try:
        await BotzHub(GetParticipantRequest(channel=CHANNEL, user_id=id))
        ok = True
    except UserNotParticipantError:
        ok = False
    return ok

if CHANNEL.startswith('@'):
    x = CHANNEL.split('@')[1]
    ltc = f"https://t.me/{x}"
else:
    ltc = CHANNEL
