// Generated from c:/Automatas_Ejercicios/competencia2/ejercicio15_Streamlit/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NMAP=1, SS=2, SUDO=3, TCPDUMP=4, CURL=5, DIG=6, JOURNALCTL=7, GREP=8, 
		UFW=9, DENY=10, FROM=11, TODAY=12, MX=13, FLAG=14, IP=15, NUM=16, CADENA=17, 
		ID=18, DIAGONAL=19, WS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NMAP", "SS", "SUDO", "TCPDUMP", "CURL", "DIG", "JOURNALCTL", "GREP", 
			"UFW", "DENY", "FROM", "TODAY", "MX", "FLAG", "IP", "NUM", "CADENA", 
			"ID", "DIAGONAL", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'nmap'", "'ss'", "'sudo'", "'tcpdump'", "'curl'", "'dig'", "'journalctl'", 
			"'grep'", "'ufw'", "'deny'", "'from'", "'today'", "'MX'", null, null, 
			null, null, null, "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NMAP", "SS", "SUDO", "TCPDUMP", "CURL", "DIG", "JOURNALCTL", "GREP", 
			"UFW", "DENY", "FROM", "TODAY", "MX", "FLAG", "IP", "NUM", "CADENA", 
			"ID", "DIAGONAL", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0014\u00ac\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\r\u0001\r\u0003\rq\b\r\u0001\r\u0004\rt\b\r\u000b"+
		"\r\f\ru\u0001\u000e\u0004\u000ey\b\u000e\u000b\u000e\f\u000ez\u0001\u000e"+
		"\u0001\u000e\u0004\u000e\u007f\b\u000e\u000b\u000e\f\u000e\u0080\u0001"+
		"\u000e\u0001\u000e\u0004\u000e\u0085\b\u000e\u000b\u000e\f\u000e\u0086"+
		"\u0001\u000e\u0001\u000e\u0004\u000e\u008b\b\u000e\u000b\u000e\f\u000e"+
		"\u008c\u0001\u000f\u0004\u000f\u0090\b\u000f\u000b\u000f\f\u000f\u0091"+
		"\u0001\u0010\u0001\u0010\u0005\u0010\u0096\b\u0010\n\u0010\f\u0010\u0099"+
		"\t\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0005\u0011\u009f"+
		"\b\u0011\n\u0011\f\u0011\u00a2\t\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0004\u0013\u00a7\b\u0013\u000b\u0013\f\u0013\u00a8\u0001\u0013\u0001"+
		"\u0013\u0000\u0000\u0014\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017"+
		"\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'"+
		"\u0014\u0001\u0000\u0005\u0002\u0000AZaz\u0001\u000009\u0003\u0000\n\n"+
		"\r\r\"\"\u0004\u0000-.09AZaz\u0003\u0000\t\n\r\r  \u00b5\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000"+
		"\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000"+
		"\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000"+
		"\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'"+
		"\u0001\u0000\u0000\u0000\u0001)\u0001\u0000\u0000\u0000\u0003.\u0001\u0000"+
		"\u0000\u0000\u00051\u0001\u0000\u0000\u0000\u00076\u0001\u0000\u0000\u0000"+
		"\t>\u0001\u0000\u0000\u0000\u000bC\u0001\u0000\u0000\u0000\rG\u0001\u0000"+
		"\u0000\u0000\u000fR\u0001\u0000\u0000\u0000\u0011W\u0001\u0000\u0000\u0000"+
		"\u0013[\u0001\u0000\u0000\u0000\u0015`\u0001\u0000\u0000\u0000\u0017e"+
		"\u0001\u0000\u0000\u0000\u0019k\u0001\u0000\u0000\u0000\u001bn\u0001\u0000"+
		"\u0000\u0000\u001dx\u0001\u0000\u0000\u0000\u001f\u008f\u0001\u0000\u0000"+
		"\u0000!\u0093\u0001\u0000\u0000\u0000#\u009c\u0001\u0000\u0000\u0000%"+
		"\u00a3\u0001\u0000\u0000\u0000\'\u00a6\u0001\u0000\u0000\u0000)*\u0005"+
		"n\u0000\u0000*+\u0005m\u0000\u0000+,\u0005a\u0000\u0000,-\u0005p\u0000"+
		"\u0000-\u0002\u0001\u0000\u0000\u0000./\u0005s\u0000\u0000/0\u0005s\u0000"+
		"\u00000\u0004\u0001\u0000\u0000\u000012\u0005s\u0000\u000023\u0005u\u0000"+
		"\u000034\u0005d\u0000\u000045\u0005o\u0000\u00005\u0006\u0001\u0000\u0000"+
		"\u000067\u0005t\u0000\u000078\u0005c\u0000\u000089\u0005p\u0000\u0000"+
		"9:\u0005d\u0000\u0000:;\u0005u\u0000\u0000;<\u0005m\u0000\u0000<=\u0005"+
		"p\u0000\u0000=\b\u0001\u0000\u0000\u0000>?\u0005c\u0000\u0000?@\u0005"+
		"u\u0000\u0000@A\u0005r\u0000\u0000AB\u0005l\u0000\u0000B\n\u0001\u0000"+
		"\u0000\u0000CD\u0005d\u0000\u0000DE\u0005i\u0000\u0000EF\u0005g\u0000"+
		"\u0000F\f\u0001\u0000\u0000\u0000GH\u0005j\u0000\u0000HI\u0005o\u0000"+
		"\u0000IJ\u0005u\u0000\u0000JK\u0005r\u0000\u0000KL\u0005n\u0000\u0000"+
		"LM\u0005a\u0000\u0000MN\u0005l\u0000\u0000NO\u0005c\u0000\u0000OP\u0005"+
		"t\u0000\u0000PQ\u0005l\u0000\u0000Q\u000e\u0001\u0000\u0000\u0000RS\u0005"+
		"g\u0000\u0000ST\u0005r\u0000\u0000TU\u0005e\u0000\u0000UV\u0005p\u0000"+
		"\u0000V\u0010\u0001\u0000\u0000\u0000WX\u0005u\u0000\u0000XY\u0005f\u0000"+
		"\u0000YZ\u0005w\u0000\u0000Z\u0012\u0001\u0000\u0000\u0000[\\\u0005d\u0000"+
		"\u0000\\]\u0005e\u0000\u0000]^\u0005n\u0000\u0000^_\u0005y\u0000\u0000"+
		"_\u0014\u0001\u0000\u0000\u0000`a\u0005f\u0000\u0000ab\u0005r\u0000\u0000"+
		"bc\u0005o\u0000\u0000cd\u0005m\u0000\u0000d\u0016\u0001\u0000\u0000\u0000"+
		"ef\u0005t\u0000\u0000fg\u0005o\u0000\u0000gh\u0005d\u0000\u0000hi\u0005"+
		"a\u0000\u0000ij\u0005y\u0000\u0000j\u0018\u0001\u0000\u0000\u0000kl\u0005"+
		"M\u0000\u0000lm\u0005X\u0000\u0000m\u001a\u0001\u0000\u0000\u0000np\u0005"+
		"-\u0000\u0000oq\u0005-\u0000\u0000po\u0001\u0000\u0000\u0000pq\u0001\u0000"+
		"\u0000\u0000qs\u0001\u0000\u0000\u0000rt\u0007\u0000\u0000\u0000sr\u0001"+
		"\u0000\u0000\u0000tu\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000"+
		"uv\u0001\u0000\u0000\u0000v\u001c\u0001\u0000\u0000\u0000wy\u0007\u0001"+
		"\u0000\u0000xw\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000zx\u0001"+
		"\u0000\u0000\u0000z{\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000"+
		"|~\u0005.\u0000\u0000}\u007f\u0007\u0001\u0000\u0000~}\u0001\u0000\u0000"+
		"\u0000\u007f\u0080\u0001\u0000\u0000\u0000\u0080~\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000\u0000"+
		"\u0082\u0084\u0005.\u0000\u0000\u0083\u0085\u0007\u0001\u0000\u0000\u0084"+
		"\u0083\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086"+
		"\u0084\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000\u0087"+
		"\u0088\u0001\u0000\u0000\u0000\u0088\u008a\u0005.\u0000\u0000\u0089\u008b"+
		"\u0007\u0001\u0000\u0000\u008a\u0089\u0001\u0000\u0000\u0000\u008b\u008c"+
		"\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000\u0000\u008c\u008d"+
		"\u0001\u0000\u0000\u0000\u008d\u001e\u0001\u0000\u0000\u0000\u008e\u0090"+
		"\u0007\u0001\u0000\u0000\u008f\u008e\u0001\u0000\u0000\u0000\u0090\u0091"+
		"\u0001\u0000\u0000\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0091\u0092"+
		"\u0001\u0000\u0000\u0000\u0092 \u0001\u0000\u0000\u0000\u0093\u0097\u0005"+
		"\"\u0000\u0000\u0094\u0096\b\u0002\u0000\u0000\u0095\u0094\u0001\u0000"+
		"\u0000\u0000\u0096\u0099\u0001\u0000\u0000\u0000\u0097\u0095\u0001\u0000"+
		"\u0000\u0000\u0097\u0098\u0001\u0000\u0000\u0000\u0098\u009a\u0001\u0000"+
		"\u0000\u0000\u0099\u0097\u0001\u0000\u0000\u0000\u009a\u009b\u0005\"\u0000"+
		"\u0000\u009b\"\u0001\u0000\u0000\u0000\u009c\u00a0\u0007\u0000\u0000\u0000"+
		"\u009d\u009f\u0007\u0003\u0000\u0000\u009e\u009d\u0001\u0000\u0000\u0000"+
		"\u009f\u00a2\u0001\u0000\u0000\u0000\u00a0\u009e\u0001\u0000\u0000\u0000"+
		"\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1$\u0001\u0000\u0000\u0000\u00a2"+
		"\u00a0\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005/\u0000\u0000\u00a4&\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a7\u0007\u0004\u0000\u0000\u00a6\u00a5\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8\u00a6\u0001"+
		"\u0000\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a9\u00aa\u0001"+
		"\u0000\u0000\u0000\u00aa\u00ab\u0006\u0013\u0000\u0000\u00ab(\u0001\u0000"+
		"\u0000\u0000\u000b\u0000puz\u0080\u0086\u008c\u0091\u0097\u00a0\u00a8"+
		"\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}