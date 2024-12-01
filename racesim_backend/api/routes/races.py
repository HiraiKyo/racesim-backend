from fastapi import APIRouter, Depends

from racesim_backend.core.deps import verify_token
from racesim_backend.core.models import CharacterRaceResult, RaceResult, RaceVisualization


router = APIRouter()



@router.get("/{race_id}/result", response_model=RaceResult)
async def get_race_result(
    race_id: str,
    user_id: str = Depends(verify_token)
):
    length = 5
    character_results = [
      CharacterRaceResult(
        character_id=f"character_id_{i}",
        race_path_id=f"race_path_id_{i}",
        finish_time=100.0 + i,
        rank=i,
        history=[]
      ) for i in range(length)
    ]

    visualization = RaceVisualization(
        main_video_url="https://example.com",
        thumbnail_url="https://example.com"
    )

    result = RaceResult(
        race_id=race_id,
        course_id="course_id_value",
        simulation_id="simulation_id_value",
        status="completed",
        character_results=character_results,
        visualization=visualization
    )
    return result