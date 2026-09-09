from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime
from .models import RoleEnum, RackStatus, AssetType, AssetStatus, VMStatus, HypervisorType, LicenseType, EventType, ChangeType, RiskLevel, ChangeStatus, ResourceType

class DataCenterBase(BaseModel):
    name: str
    location: str
    total_racks: int = 0
    total_power_kw: float = 0.0
    cooling_capacity_kw: float = 0.0
    status: str = "ACTIVE"

class DataCenterCreate(DataCenterBase):
    pass

class DataCenter(DataCenterBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class RackBase(BaseModel):
    name: str
    row_label: str
    position: str
    total_units: int = 42
    used_units: int = 0
    power_capacity_w: float = 0.0
    status: RackStatus = RackStatus.ACTIVE

class RackCreate(RackBase):
    datacenter_id: int

class Rack(RackBase):
    id: int
    datacenter_id: int
    current_power_w: float
    temperature_c: float
    class Config:
        from_attributes = True

class AssetBase(BaseModel):
    asset_tag: str
    asset_type: AssetType
    manufacturer: str
    model: str
    serial_number: str
    hostname: Optional[str] = None
    ip_address: Optional[str] = None
    os_type: Optional[str] = None
    cpu_cores: int = 0
    ram_gb: int = 0
    storage_gb: int = 0
    status: AssetStatus = AssetStatus.ORDERED
    location_notes: Optional[str] = None

class AssetCreate(AssetBase):
    rack_id: Optional[int] = None
    purchased_at: Optional[datetime] = None
    warranty_expires: Optional[datetime] = None

class Asset(AssetBase):
    id: int
    rack_id: Optional[int]
    deployed_at: Optional[datetime]
    retired_at: Optional[datetime]
    class Config:
        from_attributes = True

class ChangeRequestBase(BaseModel):
    title: str
    description: str
    requester: str
    asset_ids: List[int]
    change_type: ChangeType
    risk_level: RiskLevel
    scheduled_date: Optional[datetime] = None

class ChangeRequestCreate(ChangeRequestBase):
    pass

class ChangeRequest(ChangeRequestBase):
    id: int
    status: ChangeStatus
    completed_date: Optional[datetime]
    approver: Optional[str]
    approval_notes: Optional[str]
    class Config:
        from_attributes = True

class VMInstanceBase(BaseModel):
    name: str
    vcpus: int = 1
    ram_gb: int = 1
    storage_gb: int = 10
    os: Optional[str] = None
    ip_address: Optional[str] = None
    status: VMStatus = VMStatus.STOPPED
    hypervisor: HypervisorType

class VMInstanceCreate(VMInstanceBase):
    host_asset_id: int

class VMInstance(VMInstanceBase):
    id: int
    host_asset_id: int
    class Config:
        from_attributes = True

class LifecycleEventBase(BaseModel):
    event_type: EventType
    performed_by: str
    notes: Optional[str] = None

class LifecycleEventCreate(LifecycleEventBase):
    pass

class LifecycleEvent(LifecycleEventBase):
    id: int
    asset_id: int
    event_date: datetime
    class Config:
        from_attributes = True
