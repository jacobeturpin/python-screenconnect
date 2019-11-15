from enum import Enum


# Update to SessionEventType
class SessionEvent(Enum):
    """ Enums for Session Events """

    Connected = 10
    Disconnected = 11

    CreatedSession = 20
    EndedSession = 21

    InitiatedJoin = 30
    InvitedGuest = 31
    AddedNote = 32

    QueuedReinstall = 40
    QueuedUninstall = 41
    QueuedInvalidateLicense = 42
    QueuedWake = 43
    QueuedCommand = 44
    QueuedMessage = 45
    QueuedGuestInfoUpdate = 46
    QueuedTool = 47
    QueuedForceDisconnect = 48

    ProcessedReinstall = 50
    ProcessedUninstall = 51
    ProcessedInvalidateLicense = 52
    ProcessedWake = 53
    ProcessedCommand = 54
    ProcessedMessage = 55
    ProcessedGuestInfoUpdate = 56
    ProcessedTool = 57
    ProcessedForceDisconnect = 58

    ModifiedName = 60
    ModifiedIsPublic = 61
    ModifiedCode = 62
    ModifiedHost = 63
    ModifiedCustomProperty = 64

    RanCommand = 70
    SentMessage = 71

    SentPrintJob = 80
    ReceivedPrintJob = 81
    CopiedText = 82
    CopiedFiles = 83
    DraggedFiles = 84
    RanFiles = 85
    SentFiles = 86


class SessionType(Enum):

    Unknown = -1
    Support = 0
    Meeting = 1
    Access = 2


class ProcessType(Enum):

    Unknown = 0
    Host = 1
    Guest = 2
