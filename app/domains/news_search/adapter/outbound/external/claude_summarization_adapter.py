import anthropic

from app.domains.news_search.application.usecase.summarization_port import SummarizationPort
from app.infrastructure.config.settings import get_settings

_MAX_CONTENT_CHARS = 8000


class ClaudeSummarizationAdapter(SummarizationPort):
    def summarize(self, content: str) -> str:
        settings = get_settings()
        client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

        truncated = content[:_MAX_CONTENT_CHARS]

        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            messages=[
                {
                    "role": "user",
                    "content": (
                        "다음 뉴스 기사 본문을 3~5문장으로 한국어 요약해줘. "
                        "요약문만 출력하고, 다른 설명은 붙이지 마.\n\n"
                        f"{truncated}"
                    ),
                }
            ],
        )

        return message.content[0].text
