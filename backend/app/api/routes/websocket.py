from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.websocket.manager import manager


router = APIRouter(
    tags=["WebSocket"],
)


@router.websocket("/ws/channels/{channel_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    channel_id: int,
):
    await manager.connect(
        channel_id,
        websocket,
    )

    try:
        while True:
            data = await websocket.receive_json()

            event_type = data.get("type")

            # Typing indicator
            if event_type == "typing":

                await manager.broadcast(
                    channel_id,
                    {
                        "type": "typing",
                        "username": data.get(
                            "username",
                            "Unknown",
                        ),
                        "is_typing": data.get(
                            "is_typing",
                            False,
                        ),
                    },
                )

            else:
                await manager.broadcast(
                    channel_id,
                    data,
                )

    except WebSocketDisconnect:

        manager.disconnect(
            channel_id,
            websocket,
        )