import json
from typing import List, Union, Iterable
from .templates import Template, QuickReply, ContextControl, Data

class SkillResponseBuilder(object):
    def __init__(self, outputs: List[Template] = None, replies: List[QuickReply] = None,
                 contextControl: ContextControl = None, data: Data = None):
        self.__dict__.update(locals())
        self.outputs = [] if self.outputs is None else self.outputs
        self.replies = [] if self.replies is None else self.replies

    def append(self, template: Union[Iterable[Template], Template]):
        def _append(template):
            if(type(template) is QuickReply):  # quickReplies
                self.replies.append(template)
            elif(type(template) is ContextControl):  # contextControl
                self.contextControl = template
            elif(type(template) is Data):  # data
                self.data = template
            else:  # outputs
                if(len(self.outputs) >= 3):
                    return "최대 3개의 output까지 담을 수 있음"
                self.outputs.append(template)
        if issubclass(type(template), Iterable):
            for t in template:
                _append(t)
        else:
            _append(template)

    def to_dict(self):
        out_dict = {}
        out_dict['version'] = '2.0'
        if len(self.outputs) > 0 or len(self.replies) > 0:
            out_dict['template'] = {}
        if len(self.outputs) > 0:
            out_dict['template']['outputs'] = [output.to_dict() for output in self.outputs]
        if len(self.replies) > 0:
            out_dict['template']['quickReplies'] = [reply.to_dict() for reply in self.replies]
        if self.contextControl is not None:
            out_dict.update(self.contextControl.to_dict())
        if self.data is not None:
            out_dict.update(self.data.to_dict())
        return out_dict

    def to_json(self, **kwargs):
        return json.dumps(self.to_dict(), **kwargs)
