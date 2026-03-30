import React, { useState, useEffect } from 'react';
import { 
  Menu, Search, PlayCircle, X, Share2, MessageCircle, 
  Home, Compass, Tv, User, ChevronRight, Clock, Zap, CheckCircle2
} from 'lucide-react';

// --- MOCK DATA (AK20 News Marathi saathi) ---

const categories = ['सर्व', 'महाराष्ट्र', 'राजकारण', 'मनोरंजन', 'क्रीडा', 'शेती व व्यवसाय'];

const breakingNews = [
  "मोठी बातमी: राज्याच्या अर्थसंकल्पात महिलांसाठी मोठी घोषणा, बहीणींच्या रकमेत वाढ होणार - मुख्यमंत्री",
  "श्री सिद्धेश्वर गड्डा यात्रा २०२५ ची जय्यत तयारी सुरु.",
  "ऊस बिल तात्काळ अदा करा अन्यथा आंदोलन करणार: राजू शेट्टी यांचा इशारा.",
  "शिक्षकांचे आंदोलन : योग्य वेळी निर्णय घेऊ - देवेंद्र फडणवीस."
];

const allLiveUpdates = [
  { time: '2 mins ago', text: 'दिव्यांगांच्या निराधारांच्या पगारात वाढ करण्याची शासनाची घोषणा.', tag: 'महाराष्ट्र' },
  { time: '15 mins ago', text: 'बीड पोलीस ॲक्शन मोडमध्ये, तपासाला गती येणार.', tag: 'गुन्हेगारी' },
  { time: '34 mins ago', text: 'मोर्चा थांबवा अन्यथा प्रतिमोर्चा काढू: लक्ष्मण हाके.', tag: 'राजकारण' },
  { time: '1 hour ago', text: 'शेअर बाजारात मोठी घसरण, गुंतवणूकदारांची चिंता वाढली.', tag: 'अर्थकारण' },
  { time: '2 hours ago', text: 'राज्यात पुढील ४८ तासात अवकाळी पावसाचा इशारा.', tag: 'हवामान' },
  { time: '3 hours ago', text: 'पुण्यात नवीन आयटी पार्क उभारण्यास मंजुरी.', tag: 'व्यवसाय' },
  { time: '4 hours ago', text: 'शेतकऱ्यांसाठी पीक विमा योजनेची मुदत वाढवली.', tag: 'शेती' },
  { time: '5 hours ago', text: 'मुंबई-पुणे एक्सप्रेसवे वर वाहतूक कोंडी.', tag: 'महाराष्ट्र' }
];

const allHeroStories = [
  {
    id: 1,
    title: "राज्यातील राजकीय घडामोडींना वेग; विधानसभा निवडणुकीच्या पार्श्वभूमीवर नेत्यांच्या गाठीभेटी वाढल्या",
    category: "राजकारण",
    image: "https://images.unsplash.com/photo-1540910419892-4a36d2c3266c?auto=format&fit=crop&q=80&w=1200",
    excerpt: "आगामी निवडणुकांच्या पार्श्वभूमीवर राज्यातील राजकीय वातावरण तापले आहे. सर्वच प्रमुख पक्षांनी मोर्चेबांधणीला सुरुवात केली असून, दररोज नव्या घडामोडी समोर येत आहेत.",
    time: "४ तासांपूर्वी"
  },
  {
    id: 2,
    title: "श्री व्हन्नलिंगेश्वर यात्रा: २५ आणि २६ मार्च रोजी कार्यक्रमांची रेलचेल",
    category: "महाराष्ट्र",
    image: "https://images.unsplash.com/photo-1605367175440-2b1eb325f6f3?auto=format&fit=crop&q=80&w=600",
    time: "६ तासांपूर्वी"
  },
  {
    id: 3,
    title: "शेतकऱ्यांसाठी आनंदाची बातमी: एफआरपी आणि उचल रकमेबाबत लवकरच तोडगा",
    category: "शेती व व्यवसाय",
    image: "https://images.unsplash.com/photo-1592982537447-6f2a6a0d6c10?auto=format&fit=crop&q=80&w=600",
    time: "८ तासांपूर्वी"
  },
  {
    id: 4,
    title: "क्रिकेट: भारताचा ऑस्ट्रेलियावर दणदणीत विजय, मालिकेत आघाडी",
    category: "क्रीडा",
    image: "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?auto=format&fit=crop&q=80&w=600",
    time: "१० तासांपूर्वी"
  },
  {
    id: 5,
    title: "नवीन मराठी चित्रपटाचा ट्रेलर रिलीज, प्रेक्षकांचा उदंड प्रतिसाद",
    category: "मनोरंजन",
    image: "https://images.unsplash.com/photo-1598899134739-24c46f58b8c0?auto=format&fit=crop&q=80&w=600",
    time: "१२ तासांपूर्वी"
  }
];

// YouTube Videos data (Working IDs with privacy-enhanced embed support)
const videos = [
  { id: 'aqz-KE-bpKQ', title: 'तर बहीणींच्या रकमेत वाढ होईल: मुख्यमंत्री यांची मोठी घोषणा', thumb: 'https://images.unsplash.com/photo-1514368297072-a0ce27c95b77?auto=format&fit=crop&q=80&w=400' },
  { id: 'M7lc1UVf-VE', title: 'श्री सिद्धेश्वर गड्डा यात्रा : 2025 ची संपूर्ण माहिती आणि तयारी', thumb: 'https://images.unsplash.com/photo-1605367175440-2b1eb325f6f3?auto=format&fit=crop&q=80&w=400' },
  { id: 'jNQXAC9IVRw', title: 'ऊस बिल तात्काळ अदा करा : शेतकरी संघटनेचा इशारा', thumb: 'https://images.unsplash.com/photo-1592982537447-6f2a6a0d6c10?auto=format&fit=crop&q=80&w=400' },
  { id: 'dQw4w9WgXcQ', title: 'विशेष मुलाखत: बीड पोलीस ॲक्शन मोडमध्ये', thumb: 'https://images.unsplash.com/photo-1555848962-6e79363ec58f?auto=format&fit=crop&q=80&w=400' }
];

export default function App() {
  const [activeVideo, setActiveVideo] = useState(null);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  
  // States for Interactive Features
  const [activeCategory, setActiveCategory] = useState('सर्व');
  const [visibleUpdatesCount, setVisibleUpdatesCount] = useState(5);
  const [toastMessage, setToastMessage] = useState('');
  const [emailInput, setEmailInput] = useState('');

  // Toast Notification System
  const showToast = (message) => {
    setToastMessage(message);
    setTimeout(() => {
      setToastMessage('');
    }, 3000);
  };

  // Filter Stories
  const filteredStories = activeCategory === 'सर्व' 
    ? allHeroStories 
    : allHeroStories.filter(story => story.category === activeCategory);

  const displayStories = filteredStories.length > 0 ? filteredStories : allHeroStories.slice(0, 1);

  // Handlers
  const handleShare = (e) => {
    e.stopPropagation();
    showToast('लिंक यशस्वीरित्या कॉपी केली!');
  };

  const handleSubscribe = () => {
    if(emailInput.trim() === '') {
      showToast('कृपया आधी तुमचा ईमेल टाका.');
      return;
    }
    showToast('सबस्क्राईब केल्याबद्दल धन्यवाद!');
    setEmailInput('');
  };

  const handleLoadMore = () => {
    if (visibleUpdatesCount >= allLiveUpdates.length) {
      showToast('सध्या आणखी नवीन बातम्या नाहीत.');
    } else {
      setVisibleUpdatesCount(prev => prev + 3);
    }
  };

  const handleSocialClick = (platform) => {
    showToast(`${platform} उघडत आहे... कृपया प्रतीक्षा करा.`);
  };

  // Scroll lock for video
  useEffect(() => {
    if (activeVideo) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }
    return () => { document.body.style.overflow = 'unset'; }
  }, [activeVideo]);

  return (
    <div className="font-sans text-black bg-white min-h-screen pb-16 md:pb-0 relative">
      <style dangerouslySetInnerHTML={{__html: `
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Tiro+Devanagari+Marathi:ital@0;1&display=swap');
        body { font-family: 'Poppins', sans-serif; }
        .marathi-text { font-family: 'Tiro Devanagari Marathi', serif; }
        .ticker-wrap { width: 100%; overflow: hidden; background-color: #000; color: #fff; white-space: nowrap; }
        .ticker { display: inline-block; animation: ticker 35s linear infinite; padding-left: 100%; }
        @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }
        .hide-scrollbar::-webkit-scrollbar { display: none; }
        .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        .line-clamp-3 { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
      `}} />

      {/* TOAST NOTIFICATION */}
      {toastMessage && (
        <div className="fixed top-24 left-1/2 transform -translate-x-1/2 z-[100] bg-gray-900 text-white px-6 py-3 rounded-full shadow-2xl flex items-center space-x-2 animate-bounce marathi-text">
          <CheckCircle2 size={20} className="text-green-400" />
          <span className="font-medium">{toastMessage}</span>
        </div>
      )}

      {/* BREAKING NEWS TICKER */}
      <div className="ticker-wrap flex items-center h-10 border-b border-gray-800 relative z-50">
        <div className="bg-[#FF0000] text-white font-bold px-4 py-2 h-full flex items-center absolute left-0 z-10 uppercase text-xs tracking-wider">
          ब्रेकिंग न्यूज
        </div>
        <div className="ticker text-sm font-medium marathi-text mt-1">
          {breakingNews.map((news, idx) => (
            <span key={idx} className="mr-12">
              <span className="text-[#FF0000] mr-2">●</span> {news}
            </span>
          ))}
        </div>
      </div>

      {/* HEADER */}
      <header className="sticky top-0 z-40 bg-white border-b border-gray-200 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16 md:h-20">
            <button className="md:hidden p-2 text-gray-600 hover:text-[#FF0000]" onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}>
              {isMobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>

            <div 
              className="flex-shrink-0 flex flex-col items-center justify-center cursor-pointer"
              onClick={() => { setActiveCategory('सर्व'); window.scrollTo(0,0); }}
            >
              <span className="text-3xl font-extrabold tracking-tighter leading-none">
                AK20<span className="text-[#FF0000]">NEWS</span>
              </span>
              <span className="text-xs font-bold tracking-widest text-gray-600 uppercase mt-0.5">
                Marathi
              </span>
            </div>

            <nav className="hidden md:flex space-x-8 h-full items-center marathi-text mt-1">
              {categories.map((item) => (
                <button 
                  key={item} 
                  onClick={() => setActiveCategory(item)}
                  className={`text-[17px] font-bold tracking-wide transition-colors py-2 border-b-2 
                    ${activeCategory === item ? 'text-[#FF0000] border-[#FF0000]' : 'text-gray-900 border-transparent hover:text-[#FF0000] hover:border-[#FF0000]'}`}
                >
                  {item}
                </button>
              ))}
            </nav>

            <div className="flex items-center space-x-4">
              <button onClick={() => showToast('सर्च फीचर लवकरच येत आहे!')} className="text-gray-600 hover:text-[#FF0000]"><Search size={20} /></button>
              <button onClick={() => showToast('प्रोफाईल लॉगिन उपलब्ध नाही.')} className="hidden md:block text-gray-600 hover:text-[#FF0000]"><User size={20} /></button>
            </div>
          </div>
        </div>

        {isMobileMenuOpen && (
          <div className="md:hidden bg-white border-b border-gray-200 marathi-text absolute w-full shadow-lg">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
               {categories.map((item) => (
                <button 
                  key={item} 
                  onClick={() => {
                    setActiveCategory(item);
                    setIsMobileMenuOpen(false);
                    window.scrollTo(0,0);
                  }}
                  className={`block w-full text-left px-3 py-2 text-lg font-bold 
                    ${activeCategory === item ? 'text-[#FF0000] bg-red-50' : 'text-gray-900 hover:text-[#FF0000] hover:bg-gray-50'}`}
                >
                  {item}
                </button>
              ))}
            </div>
          </div>
        )}
      </header>

      {/* MAIN CONTENT */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex flex-col lg:flex-row gap-8">
          
          <div className="w-full lg:w-3/4">
            
            <section className="mb-12">
              <div className="flex items-center justify-between mb-4 border-b-2 border-black pb-2 marathi-text">
                <h2 className="text-2xl font-bold tracking-tight text-gray-900">
                  {activeCategory === 'सर्व' ? 'आजची मोठी बातमी' : `${activeCategory} च्या बातम्या`}
                </h2>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <article 
                  className="md:col-span-2 relative group cursor-pointer"
                  onClick={() => showToast('बातमी उघडत आहे...')}
                >
                  <div className="relative h-[400px] md:h-[500px] w-full overflow-hidden rounded-sm">
                    <img 
                      src={displayStories[0].image} 
                      alt={displayStories[0].title} 
                      className="object-cover w-full h-full transform transition-transform duration-700 group-hover:scale-105"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent"></div>
                    <div className="absolute bottom-0 left-0 p-6 w-full marathi-text">
                      <span className="bg-[#FF0000] text-white text-sm font-bold px-2 py-1 mb-3 inline-block">
                        {displayStories[0].category}
                      </span>
                      <h3 className="text-white text-2xl md:text-3xl font-bold leading-tight mb-3 group-hover:text-gray-200">
                        {displayStories[0].title}
                      </h3>
                      <p className="text-gray-300 text-lg hidden md:block mb-4 line-clamp-3 w-11/12">
                        {displayStories[0].excerpt || "सविस्तर बातमी वाचण्यासाठी येथे क्लिक करा. ताज्या घडामोडी आणि अपडेट्ससाठी आमच्यासोबत जोडलेले राहा."}
                      </p>
                      <div className="flex items-center text-gray-400 font-sans text-xs font-medium space-x-4">
                        <span className="flex items-center"><Clock size={14} className="mr-1" /> {displayStories[0].time}</span>
                        <button 
                          onClick={handleShare}
                          className="flex items-center hover:text-white transition-colors p-1"
                        >
                          <Share2 size={14} className="mr-1" /> Share
                        </button>
                      </div>
                    </div>
                  </div>
                </article>

                <div className="flex flex-col gap-6">
                  {displayStories.slice(1, 3).map((story) => (
                    <article 
                      key={story.id} 
                      className="group cursor-pointer flex flex-col h-full marathi-text"
                      onClick={() => showToast('बातमी उघडत आहे...')}
                    >
                      <div className="relative h-48 w-full overflow-hidden rounded-sm mb-3">
                        <img 
                          src={story.image} 
                          alt={story.title} 
                          className="object-cover w-full h-full transform transition-transform duration-700 group-hover:scale-105"
                        />
                        <span className="absolute top-2 left-2 bg-black text-white text-xs font-bold px-2 py-1 font-sans">
                          {story.category}
                        </span>
                      </div>
                      <h3 className="text-xl font-bold leading-snug group-hover:text-[#FF0000] transition-colors flex-grow">
                        {story.title}
                      </h3>
                      <div className="flex items-center text-gray-500 text-xs font-sans font-medium mt-2 space-x-4">
                        <span className="flex items-center"><Clock size={12} className="mr-1" /> {story.time}</span>
                        <button 
                          onClick={handleShare}
                          className="flex items-center hover:text-[#FF0000] transition-colors p-1"
                        >
                          <Share2 size={12} className="mr-1" /> Share
                        </button>
                      </div>
                    </article>
                  ))}
                </div>
              </div>
            </section>

            {/* YOUTUBE VIDEO HUB */}
            <section className="mb-12">
               <div className="flex items-center justify-between mb-4 border-b-2 border-black pb-2 marathi-text">
                <h2 className="text-2xl font-bold tracking-tight flex items-center text-gray-900">
                  <PlayCircle className="mr-2 text-[#FF0000]" /> व्हिडिओ बातम्या
                </h2>
                <a 
                  href="https://youtube.com/@ak20news41?si=YhXvZtTILV-3dLPo" 
                  target="_blank" 
                  rel="noreferrer" 
                  className="text-sm font-bold text-gray-500 hover:text-[#FF0000] flex items-center font-sans bg-gray-100 px-3 py-1 rounded-full"
                >
                  चॅनेल पहा <ChevronRight size={16} />
                </a>
              </div>
              
              <div className="flex overflow-x-auto hide-scrollbar gap-4 pb-4 snap-x">
                {videos.map((video) => (
                  <div 
                    key={video.id} 
                    className="min-w-[280px] md:min-w-[320px] snap-start group cursor-pointer relative"
                    onClick={() => setActiveVideo(video.id)}
                  >
                    <div className="relative rounded-md overflow-hidden bg-black aspect-video border border-gray-200">
                      <img 
                        src={video.thumb} 
                        alt={video.title} 
                        className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-transform duration-500 group-hover:scale-105"
                      />
                      <div className="absolute inset-0 flex items-center justify-center">
                        <div className="bg-[#FF0000]/90 p-3 rounded-full transform group-hover:scale-110 transition-transform shadow-lg">
                           <PlayCircle size={32} className="text-white" fill="currentColor" />
                        </div>
                      </div>
                      <div className="absolute bottom-2 right-2 bg-black/80 text-white text-xs px-2 py-1 rounded font-medium font-sans flex items-center">
                        <PlayCircle size={12} className="mr-1" /> Play Now
                      </div>
                    </div>
                    <h3 className="mt-3 font-bold text-[17px] leading-snug group-hover:text-[#FF0000] line-clamp-2 whitespace-normal marathi-text transition-colors">
                      {video.title}
                    </h3>
                  </div>
                ))}
              </div>
            </section>

          </div>

          <aside className="w-full lg:w-1/4">
             <div className="sticky top-24 space-y-8">
                
                <div className="bg-gray-50 border border-gray-200 p-5 rounded-sm">
                  <div className="flex items-center mb-6 marathi-text">
                    <span className="relative flex h-3 w-3 mr-3">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#FF0000] opacity-75"></span>
                      <span className="relative inline-flex rounded-full h-3 w-3 bg-[#FF0000]"></span>
                    </span>
                    <h2 className="text-xl font-bold tracking-tight text-gray-900 mt-1">लाईव्ह अपडेट्स</h2>
                  </div>
                  
                  <div className="space-y-6 relative before:absolute before:inset-0 before:ml-1.5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-gray-300 before:to-transparent">
                    {allLiveUpdates.slice(0, visibleUpdatesCount).map((update, idx) => (
                      <div key={idx} className="relative flex items-start gap-4 z-10 animate-fade-in-up">
                        <div className="absolute -left-1.5 md:left-auto md:right-auto mt-1.5 w-3 h-3 rounded-full bg-white border-2 border-[#FF0000] shadow"></div>
                        <div className="pl-6 md:pl-0 w-full">
                          <div className="flex items-center justify-between text-xs mb-1 font-sans w-full">
                            <span className="text-[#FF0000] font-bold marathi-text">{update.tag}</span>
                            <span className="text-gray-500 flex items-center"><Clock size={10} className="mr-1"/> {update.time}</span>
                          </div>
                          <p className="text-[15px] font-medium leading-snug text-gray-900 marathi-text cursor-pointer hover:text-[#FF0000] transition-colors" onClick={() => showToast('अपडेट उघडत आहे...')}>
                            {update.text}
                          </p>
                        </div>
                      </div>
                    ))}
                  </div>
                  
                  <button 
                    onClick={handleLoadMore}
                    className="w-full mt-6 py-2 border-2 border-black text-black font-bold uppercase text-xs hover:bg-black hover:text-white transition-all marathi-text text-sm active:scale-95"
                  >
                    {visibleUpdatesCount >= allLiveUpdates.length ? 'सर्व अपडेट्स संपले' : 'अधिक बातम्या वाचा'}
                  </button>
                </div>

             </div>
          </aside>

        </div>
      </main>

      {/* --- YOUTUBE LIGHTBOX MODAL (FIXED FOR PREVIEW ENVIRONMENT) --- */}
      {activeVideo && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/95 p-2 md:p-4 backdrop-blur-sm animate-fade-in">
          <button 
            onClick={() => setActiveVideo(null)}
            className="absolute top-4 right-4 md:top-8 md:right-8 text-white hover:text-[#FF0000] bg-white/10 rounded-full p-2 transition-colors z-50 shadow-lg"
          >
            <X size={32} />
          </button>
          
          <div className="w-full max-w-5xl aspect-video bg-black shadow-2xl rounded-lg overflow-hidden border border-gray-800 relative flex items-center justify-center">
            {/* FIX: Using youtube-nocookie.com avoids cross-origin tracking blocks 
               which commonly happen in testing/preview environments 
            */}
            <iframe 
              width="100%" 
              height="100%" 
              src={`https://www.youtube-nocookie.com/embed/${activeVideo}?autoplay=1&rel=0&modestbranding=1`} 
              title="AK20 News Marathi YouTube Video" 
              frameBorder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
              allowFullScreen
              className="absolute inset-0 w-full h-full"
            ></iframe>
          </div>
        </div>
      )}

      {/* FLOATING CTA */}
      <div className="fixed bottom-20 md:bottom-8 right-4 z-40 flex flex-col gap-3">
        <button 
          onClick={() => handleSocialClick('WhatsApp')}
          className="bg-[#25D366] text-white p-3 rounded-full shadow-lg hover:scale-110 active:scale-95 transition-all flex items-center group relative"
        >
          <MessageCircle size={24} />
          <span className="absolute right-full mr-4 bg-gray-900 text-white text-[13px] px-3 py-1.5 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap pointer-events-none font-medium marathi-text">
            WhatsApp ग्रुप जॉईन करा
          </span>
        </button>
        <button 
          onClick={() => handleSocialClick('Telegram')}
          className="bg-[#0088cc] text-white p-3 rounded-full shadow-lg hover:scale-110 active:scale-95 transition-all flex items-center group relative"
        >
          <Zap size={24} fill="currentColor" />
          <span className="absolute right-full mr-4 bg-gray-900 text-white text-[13px] px-3 py-1.5 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap pointer-events-none font-medium marathi-text">
            Telegram चॅनेल जॉईन करा
          </span>
        </button>
      </div>

      {/* MOBILE BOTTOM NAVIGATION */}
      <nav className="md:hidden fixed bottom-0 left-0 w-full bg-white border-t border-gray-200 z-50 flex justify-around items-center h-16 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]">
        <button 
          onClick={() => { setActiveCategory('सर्व'); window.scrollTo(0,0); }}
          className={`flex flex-col items-center justify-center w-full h-full ${activeCategory === 'सर्व' ? 'text-[#FF0000]' : 'text-gray-500 hover:text-black'}`}
        >
          <Home size={24} className="mb-1" />
          <span className="text-[11px] font-bold tracking-wide marathi-text">मुख्यपृष्ठ</span>
        </button>
        <button 
          onClick={() => { setActiveCategory('महाराष्ट्र'); window.scrollTo(0,0); }}
          className={`flex flex-col items-center justify-center w-full h-full ${activeCategory === 'महाराष्ट्र' ? 'text-[#FF0000]' : 'text-gray-500 hover:text-black'}`}
        >
          <Compass size={24} className="mb-1" />
          <span className="text-[11px] font-bold tracking-wide marathi-text">महाराष्ट्र</span>
        </button>
        <button 
          onClick={() => { document.querySelector('.snap-x').scrollIntoView({behavior: 'smooth'}); }}
          className="flex flex-col items-center justify-center w-full h-full text-gray-500 hover:text-[#FF0000]"
        >
          <Tv size={24} className="mb-1" />
          <span className="text-[11px] font-bold tracking-wide marathi-text">व्हिडिओ</span>
        </button>
        <button 
          onClick={() => showToast('प्रोफाईल सेटिंग्ज उपलब्ध नाहीत')}
          className="flex flex-col items-center justify-center w-full h-full text-gray-500 hover:text-black"
        >
          <User size={24} className="mb-1" />
          <span className="text-[11px] font-bold tracking-wide marathi-text">प्रोफाईल</span>
        </button>
      </nav>

      {/* FOOTER */}
      <footer className="bg-black text-white pt-16 pb-8 md:pb-16 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12 border-b border-gray-800 pb-12">
            <div className="md:col-span-1">
              <span className="text-3xl font-extrabold tracking-tighter block mb-1">
                AK20<span className="text-[#FF0000]">NEWS</span>
              </span>
              <span className="text-sm font-bold tracking-widest text-gray-400 uppercase block mb-4">
                Marathi
              </span>
              <p className="text-gray-400 text-[15px] leading-relaxed mb-6 marathi-text">
                राजकारण, समाजकारण, तंत्रज्ञान आणि मनोरंजन क्षेत्रातील सर्वात जलद आणि अचूक बातम्या आता एकाच क्लिकवर.
              </p>
            </div>
            <div>
              <h4 className="text-lg font-bold uppercase mb-4 tracking-wider marathi-text">कॅटेगरीज</h4>
              <ul className="space-y-2 text-sm text-gray-400 marathi-text text-[15px]">
                {categories.slice(1).map(cat => (
                  <li key={cat}>
                    <button onClick={() => { setActiveCategory(cat); window.scrollTo(0,0); }} className="hover:text-white transition-colors">{cat}</button>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h4 className="text-lg font-bold uppercase mb-4 tracking-wider marathi-text">आमच्याबद्दल</h4>
              <ul className="space-y-2 text-sm text-gray-400 marathi-text text-[15px]">
                <li><button onClick={() => showToast('संपर्क पृष्ठ उघडत आहे...')} className="hover:text-white transition-colors">संपर्क करा</button></li>
                <li><button onClick={() => showToast('जाहिरात पृष्ठ उघडत आहे...')} className="hover:text-white transition-colors">जाहिरात द्या</button></li>
                <li><button onClick={() => showToast('आमची टीम पृष्ठ उघडत आहे...')} className="hover:text-white transition-colors">आमची टीम</button></li>
              </ul>
            </div>
            <div>
               <h4 className="text-lg font-bold uppercase mb-4 tracking-wider marathi-text">न्यूजलेटर</h4>
               <p className="text-gray-400 text-[14px] mb-4 marathi-text">महत्वाच्या बातम्यांचा अलर्ट मिळवण्यासाठी सबस्क्राईब करा.</p>
               <div className="flex font-sans">
                 <input 
                   type="email" 
                   value={emailInput}
                   onChange={(e) => setEmailInput(e.target.value)}
                   placeholder="Email address" 
                   className="bg-gray-900 border border-gray-700 px-4 py-2 w-full text-sm focus:outline-none focus:border-[#FF0000] text-white" 
                 />
                 <button 
                   onClick={handleSubscribe}
                   className="bg-[#FF0000] text-white px-4 py-2 text-sm font-bold uppercase hover:bg-red-700 transition-colors active:bg-red-800"
                 >
                   Subscribe
                 </button>
               </div>
            </div>
          </div>
          <div className="flex flex-col md:flex-row justify-between items-center text-gray-500 text-xs font-medium">
            <p>&copy; {new Date().getFullYear()} AK20 News Marathi. All rights reserved.</p>
            <div className="flex space-x-6 mt-4 md:mt-0 marathi-text text-sm">
              <button onClick={() => showToast('गोपनीयता धोरण...')} className="hover:text-white">गोपनीयता (Privacy)</button>
              <button onClick={() => showToast('अटी आणि शर्ती...')} className="hover:text-white">अटी (Terms)</button>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}


