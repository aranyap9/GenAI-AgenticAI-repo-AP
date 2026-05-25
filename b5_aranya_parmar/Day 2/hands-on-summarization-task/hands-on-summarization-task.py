from transformers import pipeline

summarizer = pipeline("summarization")

large_text = """
Research shows considering the legacy we are leaving behind can help us improve our mental health and find more meaning during our lives including if we are still young.

When Beth Hunter's father was diagnosed with Alzheimer's disease, she asked him whether she could record them having a conversation, so she could listen back to it in years to come.

He refused. He wasn't the type to have deep heart-to-hearts about their relationship, Hunter says he didn't confront his diagnosis or talk about death. Instead, he prioritised writing his war stories, and did so by hand, before hiring someone else to type them. This is what he felt was most valuable to pass on after his death.

While leaving a legacy may feel more urgent for older adults who feel the pressing nature of limited time, some scholars argue the drive to leave one can and maybe should begin earlier in life. And a growing body of research suggests that better understanding our innate human interest in passing something on to future generations after we die could reveal new ways to improve mental health.

"The vast majority of people don't think about it," says Hunter, who is an associate professor at Bowling Green State University, Ohio, US, and an expert in legacy in the context of cancer survivorship.


But legacy can manifest in different ways and even be an unconscious act. "Everyone leaves a legacy, whether you know it or not," says Hunter. It isn't just the bequeathment of wealth or property, or everlasting art such as music or writing. Instead, some researchers have split legacy into three main overlapping categories: biological legacy, which we leave through our bodies and genetics, material legacy, represented by our wealth and possessions, and the legacy of our values, such as faith, culture and heritage.

A bodily legacy
For many, the most obvious form of biological legacy is passing on genetics through having biological children. But genetic lineage, which refers to an ancestral line connected through genes, and legacy, our lasting impact after death, can be two separate things.

Leaving a biological legacy may also involve leaving the very shells we live in: our bodies. About 170 million Americans are registered organ donors, though only three in every 1,000 people die in circumstances that allow for a successful organ donation. Some people wish to even donate their whole bodies to science, meaning their bodies will be used to educate medical students or for research, such as the development of new clinical procedures. In the US in 2021, more than 26,000 body donations were received.
"""

summary = summarizer(
    large_text,
    max_length = 80,
    min_length = 30,
    do_sample = False
)

print("===== SUMMARY =====")
print(summary[0]['summary_text'])