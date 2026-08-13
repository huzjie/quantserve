# -*- coding: utf-8 -*-
"""QuantServe exception hierarchy."""


class QuantServeError(Exception):
    """Base error for all QuantServe failures."""


class ConfigError(QuantServeError):
    """Configuration is missing or invalid."""


class DownloadError(QuantServeError):
    """Weight download failed (network / checksum / quota)."""


class ChecksumError(DownloadError):
    """Downloaded file failed integrity verification."""


class QuantizationError(QuantServeError):
    """Quantization planning or execution failed."""


class EngineError(QuantServeError):
    """Inference engine not found or failed to launch."""


class PlanError(QuantServeError):
    """Parallel / topology planning failed."""


class ServeError(QuantServeError):
    """Serving gateway failed."""


class NotFoundError(QuantServeError):
    """Requested model / engine / job not found."""


class AuthError(QuantServeError):
    """Authentication / authorization failure."""
