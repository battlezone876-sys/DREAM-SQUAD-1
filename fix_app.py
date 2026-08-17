import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# We need to find the specific block where things went wrong.
# Let's search for "Paid Match\n                    </button>"
# and up to "          <div className=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pt-2\">"

pattern = re.compile(r'Paid Match\s*</button>.*?<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pt-2">', re.DOTALL)

replacement = """Paid Match
                    </button>
                    <button
                      onClick={() => setSelectedType('free')}
                      className={`px-3 py-1.5 rounded-lg transition cursor-pointer ${
                        selectedType === 'free' ? 'bg-emerald-600 text-white font-bold' : 'text-neutral-400 hover:text-white'
                      }`}
                    >
                      Free Entry
                    </button>
                  </div>
                </div>
              </div>

              {/* Tournament Grid */}
              {filteredTournaments.length === 0 ? (
                <div className="py-16 text-center rounded-3xl bg-neutral-900/50 border border-neutral-800 space-y-2">
                  <Flame className="w-10 h-10 mx-auto text-neutral-600" />
                  <p className="text-sm font-semibold text-neutral-400">কোনো টুর্নামেন্ট পাওয়া যায়নি</p>
                </div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 sm:gap-6">
                  {filteredTournaments.map((tour) => (
                    <TournamentCard key={tour.id} tournament={tour} />
                  ))}
                </div>
              )}
            </section>
          )}
        </main>
      )}

      {/* VIEW: TOURNAMENTS (Dedicated Match Explorer with Mode Groups) */}
      {currentView === 'tournaments' && (
        <main className="flex-1 w-full min-w-0 max-w-7xl mx-auto px-4 sm:px-6 py-6 space-y-6">
          <div className="flex items-center justify-between mb-2 sm:mb-4">
            <button
              onClick={() => setCurrentView('home')}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-400 hover:text-white hover:bg-neutral-800 transition cursor-pointer text-[10px] sm:text-xs font-bold"
            >
              <ArrowLeft className="w-3.5 h-3.5" /> Back
            </button>

            {/* Solo/Duo/Squad Mode Filter in Center */}
            <div className="flex items-center gap-1 bg-neutral-900 p-1 rounded-full border border-neutral-800">
              {(['all', 'Solo', 'Duo', 'Squad'] as const).map((m) => (
                <button
                  key={m}
                  onClick={() => setSelectedModeFilter(m)}
                  className={`px-3 sm:px-4 py-1 sm:py-1.5 rounded-full transition cursor-pointer text-[10px] sm:text-xs font-bold ${
                    selectedModeFilter === m
                       ? 'bg-indigo-500 text-white shadow-md'
                       : 'text-neutral-400 hover:text-white'
                  }`}
                >
                  {m === 'all' ? 'ALL' : m.toUpperCase()}
                </button>
              ))}
            </div>

            <button
              onClick={() => setCurrentView('results')}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-neutral-900 border border-neutral-800 text-amber-400 hover:text-amber-300 hover:bg-neutral-800 transition cursor-pointer text-[10px] sm:text-xs font-bold"
            >
              <Trophy className="w-3.5 h-3.5" /> Results
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pt-2">"""

new_content = pattern.sub(replacement, content)

with open('src/App.tsx', 'w') as f:
    f.write(new_content)
print("done")
