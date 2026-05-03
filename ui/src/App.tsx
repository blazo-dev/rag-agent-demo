import type { KeyboardEvent } from 'react'
import { useEffect, useRef, useState } from 'react'

type Message = {
  id: string
  role: 'bot' | 'user'
  text: string
  time: string
}

const formatTime = (date: Date) =>
  date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })

const createId = () =>
  typeof crypto !== 'undefined' && crypto.randomUUID
    ? crypto.randomUUID()
    : `${Date.now()}-${Math.random().toString(16).slice(2)}`

function App() {
  const [messages, setMessages] = useState<Message[]>(() => [
    {
      id: createId(),
      role: 'bot',
      text:
        "Hi! I'm Bryan's professional assistant. I can tell you about his experience in AWS, React, or his software development projects. What would you like to know?",
      time: formatTime(new Date()),
    },
  ])
  const [input, setInput] = useState('')
  const [isTyping, setIsTyping] = useState(false)
  const endRef = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isTyping])

  const handleSend = async () => {
    const trimmed = input.trim()
    if (!trimmed || isTyping) return

    const userMessage: Message = {
      id: createId(),
      role: 'user',
      text: trimmed,
      time: formatTime(new Date()),
    }

    setInput('')
    setMessages((prev) => [...prev, userMessage])
    setIsTyping(true)

    try {
      const response = await fetch('http://localhost:8001/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: trimmed }),
      })

      if (!response.ok) {
        throw new Error('Request failed')
      }

      const data = await response.json()
      const botText = typeof data?.response === 'string' ? data.response : ''

      if (!botText) {
        throw new Error('Empty response')
      }

      setMessages((prev) => [
        ...prev,
        {
          id: createId(),
          role: 'bot',
          text: botText,
          time: formatTime(new Date()),
        },
      ])
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          id: createId(),
          role: 'bot',
          text: 'Sorry, I could not connect to the server.',
          time: formatTime(new Date()),
        },
      ])
    } finally {
      setIsTyping(false)
    }
  }

  const handleKeyDown = (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter') {
      event.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col">
      <header className="w-full bg-white/90 border-b border-slate-200">
        <div className="max-w-4xl mx-auto px-6 py-4 grid grid-cols-[auto,1fr,auto] items-center gap-4">
          <div className="flex gap-4 items-center">
            <div className="h-11 w-11 rounded-full bg-blue-600 text-white flex items-center justify-center text-base font-semibold">
              BL
            </div>
            <h1 className="text-lg font-semibold text-slate-900">
              Bryan's Professional Bot
            </h1>
          </div>
        </div>
      </header>

      <main className="flex-1 overflow-y-auto">
        <div className="max-w-4xl mx-auto px-6 py-6 space-y-5">
          {messages.map((message) => {
            const isUser = message.role === 'user'

            return (
              <div
                key={message.id}
                className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}
              >
                <div className="max-w-[82%]">
                  <div
                    className={`px-4 py-3 text-base leading-relaxed ${isUser
                      ? 'bg-blue-600 text-white rounded-2xl rounded-br-none'
                      : 'bg-slate-100 text-slate-800 rounded-2xl rounded-bl-none'
                      }`}
                  >
                    {message.text}
                  </div>
                  <div
                    className={`mt-2 text-sm ${isUser
                      ? 'text-right text-slate-400'
                      : 'text-left text-slate-500'
                      }`}
                  >
                    {message.time}
                  </div>
                </div>
              </div>
            )
          })}

          {isTyping ? (
            <div className="flex justify-start">
              <div className="bg-slate-100 text-slate-700 rounded-2xl rounded-bl-none px-4 py-3">
                <div className="flex items-center gap-1.5">
                  <span className="h-2.5 w-2.5 rounded-full bg-slate-400 animate-bounce" />
                  <span className="h-2.5 w-2.5 rounded-full bg-slate-400 animate-bounce [animation-delay:150ms]" />
                  <span className="h-2.5 w-2.5 rounded-full bg-slate-400 animate-bounce [animation-delay:300ms]" />
                </div>
              </div>
            </div>
          ) : null}
          <div ref={endRef} />
        </div>
      </main>

      <div className="sticky bottom-0 w-full bg-white border-t border-slate-200">
        <div className="max-w-4xl mx-auto px-6 py-4">
          <div className="flex items-center gap-3 bg-slate-100 border border-slate-200 rounded-xl px-4 py-3 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-100">
            <input
              type="text"
              value={input}
              onChange={(event) => setInput(event.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Write your question..."
              className="flex-1 bg-transparent text-base text-slate-700 placeholder:text-slate-400 outline-none"
              aria-label="Message"
            />
            <button
              type="button"
              onClick={handleSend}
              disabled={isTyping || !input.trim()}
              className="h-10 w-10 rounded-lg bg-blue-600 text-white flex items-center justify-center hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
              aria-label="Send message"
            >
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="h-4.5 w-4.5"
                aria-hidden="true"
              >
                <path d="M22 2L11 13" />
                <path d="M22 2L15 22L11 13L2 9L22 2Z" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
