from typing import List, Literal, Optional
from pydantic import BaseModel, Field

class Point2D(BaseModel):
    x: float = Field(..., description="X(コース方向)")
    y: float = Field(..., description="Y(コース垂直方向)")

class MarkerPosition(BaseModel):
    position: Point2D = Field(..., description="マーカー位置")
    stamina_used: float = Field(..., ge=0, description="マーカー間の消費スタミナ量")

class Character(BaseModel):
    id: str
    name: str
    max_stamina: float = Field(..., ge=0, description="キャラクタースタミナ総量")
    speed: float = Field(..., gt=0, description="キャラクター最大速度")
    acceleration: float = Field(..., gt=0, description="キャラクター加速")

class Course(BaseModel):
    id: str
    name: str
    length: float = Field(..., gt=0, description="コース長さ")

class RacePath(BaseModel):
    id: str
    character_id: str
    course_id: str
    markers: list[MarkerPosition]

class Race(BaseModel):
    id: str

class CharacterState(BaseModel):
    timestamp: float = Field(..., ge=0, description="タイムスタンプ")
    position: Point2D = Field(..., description="キャラクター位置")
    velocity: Point2D = Field(..., description="キャラクター速度")
    stamina: float = Field(..., ge=0, description="キャラクタースタミナ残量")
    rank: int = Field(..., ge=1, description="順位")

class CharacterRaceResult(BaseModel):
    character_id: str
    race_path_id: str
    finish_time: float = Field(..., gt=0, description="走破タイム")
    rank: int = Field(..., ge=1, description="順位")
    history: List[CharacterState] = Field(..., description="キャラクター状態履歴")

class RaceVisualization(BaseModel):
    main_video_url: str = Field(..., description="レース動画URL (Cloud Storage)")
    thumbnail_url: str = Field(..., description="サムネイル画像URL (Cloud Storage)")

class RaceResult(BaseModel):
    race_id: str
    course_id: str
    simulation_id: str
    status: Literal["pending", "running", "completed", "failed"] = Field(
        ...,
        description="シミュレーション動画生成状況"
    )

    character_results: List[CharacterRaceResult]

    visualization: RaceVisualization

    error_message: Optional[str] = None