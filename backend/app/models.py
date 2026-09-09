import os
import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, JSON, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    OPERATOR = "OPERATOR"
    VIEWER = "VIEWER"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.VIEWER)

class DataCenter(Base):
    __tablename__ = "datacenters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    total_racks = Column(Integer, default=0)
    total_power_kw = Column(Float, default=0.0)
    cooling_capacity_kw = Column(Float, default=0.0)
    status = Column(String, default="ACTIVE")
    created_at = Column(DateTime, default=datetime.utcnow)
    racks = relationship("Rack", back_populates="datacenter")

class RackStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    MAINTENANCE = "MAINTENANCE"
    DECOMMISSIONED = "DECOMMISSIONED"

class Rack(Base):
    __tablename__ = "racks"
    id = Column(Integer, primary_key=True, index=True)
    datacenter_id = Column(Integer, ForeignKey("datacenters.id"))
    name = Column(String, index=True)
    row_label = Column(String)
    position = Column(String)
    total_units = Column(Integer, default=42)
    used_units = Column(Integer, default=0)
    power_capacity_w = Column(Float, default=0.0)
    current_power_w = Column(Float, default=0.0)
    temperature_c = Column(Float, default=0.0)
    status = Column(Enum(RackStatus), default=RackStatus.ACTIVE)
    datacenter = relationship("DataCenter", back_populates="racks")
    assets = relationship("Asset", back_populates="rack")

class AssetType(str, enum.Enum):
    SERVER = "SERVER"
    SWITCH = "SWITCH"
    ROUTER = "ROUTER"
    STORAGE = "STORAGE"
    PDU = "PDU"
    UPS = "UPS"
    VM = "VM"
    OTHER = "OTHER"

class AssetStatus(str, enum.Enum):
    ORDERED = "ORDERED"
    RECEIVED = "RECEIVED"
    DEPLOYED = "DEPLOYED"
    MAINTENANCE = "MAINTENANCE"
    RETIRED = "RETIRED"
    DISPOSED = "DISPOSED"

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    rack_id = Column(Integer, ForeignKey("racks.id"), nullable=True)
    asset_tag = Column(String, unique=True, index=True)
    asset_type = Column(Enum(AssetType))
    manufacturer = Column(String)
    model = Column(String)
    serial_number = Column(String)
    hostname = Column(String)
    ip_address = Column(String)
    os_type = Column(String)
    cpu_cores = Column(Integer, default=0)
    ram_gb = Column(Integer, default=0)
    storage_gb = Column(Integer, default=0)
    status = Column(Enum(AssetStatus), default=AssetStatus.ORDERED)
    location_notes = Column(String)
    purchased_at = Column(DateTime, nullable=True)
    warranty_expires = Column(DateTime, nullable=True)
    deployed_at = Column(DateTime, nullable=True)
    retired_at = Column(DateTime, nullable=True)
    rack = relationship("Rack", back_populates="assets")
    vms = relationship("VMInstance", back_populates="host_asset")
    licenses = relationship("License", back_populates="asset")
    lifecycle_events = relationship("LifecycleEvent", back_populates="asset")

class VMStatus(str, enum.Enum):
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    SUSPENDED = "SUSPENDED"
    MIGRATING = "MIGRATING"

class HypervisorType(str, enum.Enum):
    ESXI = "ESXI"
    PROXMOX = "PROXMOX"
    HYPERV = "HYPERV"
    KVM = "KVM"

class VMInstance(Base):
    __tablename__ = "vminstances"
    id = Column(Integer, primary_key=True, index=True)
    host_asset_id = Column(Integer, ForeignKey("assets.id"))
    name = Column(String, index=True)
    vcpus = Column(Integer, default=1)
    ram_gb = Column(Integer, default=1)
    storage_gb = Column(Integer, default=10)
    os = Column(String)
    ip_address = Column(String)
    status = Column(Enum(VMStatus), default=VMStatus.STOPPED)
    hypervisor = Column(Enum(HypervisorType))
    host_asset = relationship("Asset", back_populates="vms")

class LicenseType(str, enum.Enum):
    PERPETUAL = "PERPETUAL"
    SUBSCRIPTION = "SUBSCRIPTION"
    TRIAL = "TRIAL"
    OPEN_SOURCE = "OPEN_SOURCE"

class License(Base):
    __tablename__ = "licenses"
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=True)
    software_name = Column(String)
    license_key = Column(String)
    license_type = Column(Enum(LicenseType))
    seats = Column(Integer, default=1)
    used_seats = Column(Integer, default=0)
    vendor = Column(String)
    cost_usd = Column(Float, default=0.0)
    purchased_at = Column(DateTime)
    expires_at = Column(DateTime, nullable=True)
    asset = relationship("Asset", back_populates="licenses")

class EventType(str, enum.Enum):
    ORDERED = "ORDERED"
    RECEIVED = "RECEIVED"
    INSTALLED = "INSTALLED"
    DEPLOYED = "DEPLOYED"
    MAINTENANCE_START = "MAINTENANCE_START"
    MAINTENANCE_END = "MAINTENANCE_END"
    RETIRED = "RETIRED"
    DISPOSED = "DISPOSED"

class LifecycleEvent(Base):
    __tablename__ = "lifecycle_events"
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    event_type = Column(Enum(EventType))
    performed_by = Column(String)
    notes = Column(String)
    event_date = Column(DateTime, default=datetime.utcnow)
    asset = relationship("Asset", back_populates="lifecycle_events")

class ChangeType(str, enum.Enum):
    HARDWARE = "HARDWARE"
    SOFTWARE = "SOFTWARE"
    NETWORK = "NETWORK"
    POWER = "POWER"
    EMERGENCY = "EMERGENCY"

class RiskLevel(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class ChangeStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"
    ROLLBACK = "ROLLBACK"

class ChangeRequest(Base):
    __tablename__ = "change_requests"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    requester = Column(String)
    asset_ids = Column(JSON)
    change_type = Column(Enum(ChangeType))
    risk_level = Column(Enum(RiskLevel))
    status = Column(Enum(ChangeStatus), default=ChangeStatus.DRAFT)
    scheduled_date = Column(DateTime, nullable=True)
    completed_date = Column(DateTime, nullable=True)
    approver = Column(String, nullable=True)
    approval_notes = Column(String, nullable=True)

class PowerReading(Base):
    __tablename__ = "power_readings"
    id = Column(Integer, primary_key=True, index=True)
    rack_id = Column(Integer, ForeignKey("racks.id"))
    power_watts = Column(Float)
    temperature_c = Column(Float)
    humidity_pct = Column(Float)
    recorded_at = Column(DateTime, default=datetime.utcnow)

class ResourceType(str, enum.Enum):
    CPU = "CPU"
    RAM = "RAM"
    STORAGE = "STORAGE"
    POWER = "POWER"

class CapacityForecast(Base):
    __tablename__ = "capacity_forecasts"
    id = Column(Integer, primary_key=True, index=True)
    datacenter_id = Column(Integer, ForeignKey("datacenters.id"))
    resource_type = Column(Enum(ResourceType))
    current_usage_pct = Column(Float)
    predicted_usage_pct = Column(Float)
    days_until_80_pct = Column(Integer, nullable=True)
    days_until_full = Column(Integer, nullable=True)
    forecast_date = Column(DateTime, default=datetime.utcnow)
